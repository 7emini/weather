import requests
import datetime
import os
import sys

from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QLabel, QWidget, QHBoxLayout, QDialog, QMessageBox, QFrame
from PySide6.QtGui import QPixmap, QPalette, QColor
from PySide6.QtCore import Qt, QSize, QThread, Signal
from window_ui import Ui_MainWindow
from table_item_ui import Ui_Form

from setting import SettingManager, SettingWindow
from about import AboutWindow


class TableItem(QWidget, Ui_Form):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.frame.setFrameShape(QFrame.Shape.NoFrame)

class WeatherListWidgetItem(QListWidgetItem):

    def __init__(self, info = None):
        super().__init__()
        self.widget = TableItem()
        if info:
            
            now = datetime.datetime.now()
            date = datetime.datetime.strptime(info['date'], '%Y-%m-%d')
            if date.date() == now.date():
                day_str = '今天'
            else:
                day_str = date.strftime('%m月%d日')

            self.widget.ui_time_label.setText(day_str)
            
            self.widget.ui_day_label.setText(info['text_day'])
            self.widget.ui_night_lable.setText(info['text_night'])

            code_night = info['code_night']
            self.widget.ui_night_img.setPixmap(QPixmap(f':/img/img/{code_night}@2x.png'))

            code_day = info['code_day']
            self.widget.ui_day_img.setPixmap(QPixmap(f':/img/img/{code_day}@2x.png'))

            tem_height = info['high']
            tem_low = info['low']
            self.widget.ui_temp_label.setText(f'{tem_low}°C 到 {tem_height}°C')
            
            humidity = info['humidity']
            self.widget.ui_hum_label.setText(f'相对湿度 {humidity}%')

            wind_direction = info['wind_direction']
            wind_speed = info['wind_speed']
            wind_scale = info['wind_scale']
            self.widget.ui_wind_label.setText(f'{wind_direction}风 {wind_scale}级 {wind_speed}km/h ')
            
        self.setSizeHint(QSize(self.widget.sizeHint().width(), 240))


class RequestThred(QThread):

    successed_signal = Signal(dict, dict)
    failed_signal = Signal(str)

    def __init__(self):
        super().__init__()

    def request_weather(self):
        sm = SettingManager()
        now_url = 'https://api.seniverse.com/v3/weather/now.json'
        daily_url = 'https://api.seniverse.com/v3/weather/daily.json'
        key = 'STcQJfCq6C1Wb7r1l'
        
        city_type = sm.getSetting('city_type')
        city = sm.getSetting('city')
        location = city if city_type == 'cus' else 'ip'
        
        params = {
            'key':key,
            'location':location,
            'language':'zh-Hans',
            'unit':'c',
            'start':'-1',
            'days':'5',
        }
        try:
            r = requests.get(url=now_url, params=params)
            data_c = r.json()
            r = requests.get(url=daily_url, params=params)
            data_d = r.json()
            self.successed_signal.emit(data_c, data_d)
        except:
            self.successed_signal.emit("提示", "请重新输入城市名称")

    
    def run(self) -> None:
        self.request_weather()

class Window(QMainWindow, Ui_MainWindow):




    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.request_thred = RequestThred()
        self.request_thred.successed_signal.connect(self.set_window_view)
        self.request_thred.failed_signal.connect(self.show_error_msg)

        self.setting_win:QDialog = None
        self.about_win:QDialog = None

        self.actionCity.triggered.connect(self.show_setting_page)
        self.actionAbout.triggered.connect(self.show_about_page)
        self.actionRefresh.triggered.connect(self.request_weather)


        # 绑定点击槽函数 点击显示对应item中的name
        self.listWidget.itemClicked.connect(lambda item: print(item))

        self.request_weather()

    
    def request_weather(self):
        self.request_thred.run()
    
    def show_error_msg(self, message):
        QMessageBox.critical(self, message)
        self.request_thred.quit()

    

    def set_window_view(self, data_c, data_d):
        weather_data = data_c['results'][0]['now']
        location_data = data_c['results'][0]['location']
        code = weather_data['code']
        temperature = weather_data['temperature']
        info = weather_data['text']
        path = location_data['path']
        

        self.ui_day_img.setPixmap(QPixmap(f':/img/img/{code}@2x.png'))
        self.ui_day_label.setText(f'{info} {temperature}°C')
        self.ui_city_label.setText(path)

        
        
        dayil_info = data_d['results'][0]['daily']
        
        self.listWidget.clear()
        # self.listWidget.clearContents()

        for info in dayil_info:
            item = WeatherListWidgetItem(info)
            # 在listWidget中加入两个自定义的item
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, item.widget)
        
        self.request_thred.quit()

    
    def show_setting_page(self):
        if self.setting_win is None:
            self.setting_win = SettingWindow(self)
        self.setting_win.show()
        self.setting_win.refresh_window.connect(self.request_weather)

    def show_about_page(self):
        if self.about_win is None:
            self.about_win = AboutWindow(self)
        self.about_win.show()


         



