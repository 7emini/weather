import sys
import json
import os
from PySide6.QtWidgets import (QWidget, QMainWindow, QApplication, QGridLayout,
    QLabel, QPushButton, QLineEdit, QSizePolicy, QMessageBox, QMenuBar, QMenu, QDialog)
from PySide6.QtCore import Qt, QObject, QSize, QRect, Signal, QFile, QByteArray
from PySide6.QtGui import QGuiApplication, QPixmap, QIcon, QPalette, QColor, QFont, QAction, QImage, QImageReader, QShortcut, QKeySequence
import image_rc
import requests
from setting_ui import Ui_Setting
from about_ui import Ui_About

class SettingManager:
    def __init__(self) -> None:
        root = os.getcwd()
        setting_file = f'{root}/setting.json'
        print(setting_file)
        self.config_file = QFile(setting_file)

        if self.config_file.exists():
            self.config_file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text)
            content = self.config_file.readAll()
            self.setting = json.loads(str(content, encoding='utf-8'))

            print(self.setting)
            
            self.config_file.close()
        else:
            print('no file')
            raise Exception('no file')


    def getSetting(self, key):
        if key in self.setting:
            return self.setting[key]
        return None
    
    def setSetting(self, key, value):
        self.setting[key] = value

    def saveSetting(self):
        json_str = json.dumps(self.setting)

        self.config_file.open(QFile.OpenModeFlag.WriteOnly | QFile.OpenModeFlag.Text)
        self.config_file.write(QByteArray(json_str))
        self.config_file.close() 

class MainWindow(QMainWindow):

    refresh_window = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()
        self.action_setting.triggered.connect(self.show_setting)
        self.action_about.triggered.connect(self.show_about)
        self.request_weather()

        
    def _setup_ui(self):

        self.setWindowTitle('天气')

        self.resize(300, 300)
        screen = QGuiApplication.primaryScreen().size()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)
        self.setMinimumSize(200, 200)
        

        self.action_setting = QAction(self)
        self.action_setting.setText('城市')
        self.action_setting.setShortcut('Ctrl+C')

        self.action_about = QAction(self)
        self.action_about.setText('关于')
        self.action_about.setShortcut("Ctrl+A")


        self.menu = QMenu(self)
        self.menu.setTitle('设置')
        self.menu.addActions([self.action_setting, self.action_about])
        

        self.menubar = QMenuBar(self)
      
        self.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())

        


        self.widget = QWidget(self)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))
        self.setPalette(palette)

        self.layout = QGridLayout(self.widget)
        self.layout.setHorizontalSpacing(5)
        self.layout.setVerticalSpacing(10)

       
        self.ui_img = QLabel(self.widget)
        
        self.ui_img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui_img.setPixmap(QPixmap(f':/weather/resource/image/99@2x.png'))

        self.ui_info = QLabel(self.widget)
        self.ui_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setPointSize(15) 
        self.ui_info.setFont(font)
        self.ui_info.setStyleSheet("color: gray;")

        self.ui_info_t = QLabel(self.widget)
        self.ui_info_t.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setPointSize(22) 
        self.ui_info_t.setFont(font)


            
        self.ui_img.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addWidget(self.ui_img, 0, 0, 1, 4)
        self.layout.addWidget(self.ui_info_t, 2, 0, 1, 4)
        self.layout.addWidget(self.ui_info, 3, 0, 1, 4)

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.setting_win:QDialog = None
        self.about_win:QDialog = None

        

    def show_setting(self):
        if self.setting_win is None:
            self.setting_win = SettingWindow(self)
        self.setting_win.show()
        self.setting_win.refresh_window.connect(self.request_weather)

    def show_about(self):
        if self.about_win is None:
            self.about_win = AboutWindow(self)
        self.about_win.show()

    def request_weather(self):
        
        sm = SettingManager()
        url = 'https://api.seniverse.com/v3/weather/now.json'
        key = 'STcQJfCq6C1Wb7r1l'
       
        city_type = sm.getSetting('city_type')
        city = sm.getSetting('city')
        location = city if city_type == 'cus' else 'ip'
        
        params = {
            'key':key,
            'location':location,
            'language':'zh-Hans',
            'unit':'c'
        }
        try:
            r = requests.get(url=url, params=params)
            data = r.json()
            weather_data = data['results'][0]['now']
            location_data = data['results'][0]['location']
            code = weather_data['code']
            temperature = weather_data['temperature']
            info = weather_data['text']
            path = location_data['path']
            

            self.ui_img.setPixmap(QPixmap(f':/weather/resource/image/{code}@2x.png'))
            self.ui_info_t.setText(f'{info} {temperature}°C')
            self.ui_info.setText(path)


        except:
            self.ui_img.setPixmap(QPixmap(f':/weather/resource/image/99@2x.png'))
            self.ui_info_t.setText('暂无数据')
            self.ui_info.setText('N/A')
            QMessageBox.critical(self, "提示", "请重新输入城市名称")

class SettingWindow(QDialog, Ui_Setting):
    refresh_window = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))
        self.setPalette(palette)

        self.sm = SettingManager()

        city_type = self.sm.getSetting('city_type')
        if city_type == 'ip':
            self.radioButton.setChecked(True)
        if city_type == 'cus':
            self.radioButton_2.setChecked(True)
        self.lineEdit.setText(self.sm.getSetting('city'))

        self.accepted.connect(self.saveSetting)
    
    def saveSetting(self):
        if self.radioButton.isChecked():
            self.sm.setSetting('city_type', 'ip')
        if self.radioButton_2.isChecked():
            self.sm.setSetting('city_type', 'cus')
        
        self.sm.setSetting('city', self.lineEdit.text())

        if self.sm.getSetting('city_type') == 'cus' and not self.sm.getSetting('city'):
            QMessageBox.critical(self, "提示", "请重新输入城市名称")
            self.setVisible(True)

        self.sm.saveSetting()

        self.refresh_window.emit()

class AboutWindow(QDialog, Ui_About):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))
        self.setPalette(palette)

        img = QImageReader(':/weather/resource/image/weather_b.png')
        scale = 100 / img.size().width()
        height = int(img.size().height() * scale)
        img.setScaledSize(QSize(100, height))
        img = img.read()
        # 打开设置好的图片
        pixmap = QPixmap(img)
        self.label.setPixmap(pixmap)

        # pixmap = QPixmap(":/weather/resource/image/weather_b.png").scaled(QSize(70, 70), aspectMode=Qt.AspectRatioMode.KeepAspectRatio)
        # self.label.setPixmap(pixmap)


    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setApplicationDisplayName('天气')
    app.setWindowIcon(QIcon(':/weather/resource/image/weather.png'))
    app.setEffectEnabled(Qt.UIEffect.UI_AnimateCombo, enable=True)
    win = MainWindow()
    win.show()
    exit_code = app.exec()
    sys.exit(exit_code)