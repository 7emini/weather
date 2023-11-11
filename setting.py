import json
from PySide6.QtWidgets import QDialog, QMessageBox, QDialogButtonBox
from PySide6.QtCore import Signal, QFile, QByteArray
from setting_ui import Ui_Setting

class SettingManager:
    def __init__(self) -> None:
        self.config_file = QFile('./setting.json')
        if self.config_file.exists():
            self.config_file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text)
            content = self.config_file.readAll()
            self.setting = json.loads(str(content, encoding='utf-8'))
            
            self.config_file.close()


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

class SettingWindow(QDialog, Ui_Setting):
    refresh_window = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.sm = SettingManager()

        city_type = self.sm.getSetting('city_type')
        if city_type == 'ip':
            self.ui_radio_curr.setChecked(True)
        if city_type == 'cus':
            self.ui_radio_cus.setChecked(True)
        self.ui_city_input.setText(self.sm.getSetting('city'))

        self.buttonBox.button(QDialogButtonBox.StandardButton.Ok).setText("确定")
        self.buttonBox.button(QDialogButtonBox.StandardButton.Cancel).setText("取消")

        self.accepted.connect(self.saveSetting)
    
    def saveSetting(self):
        if self.ui_radio_curr.isChecked():
            self.sm.setSetting('city_type', 'ip')
        if self.ui_radio_cus.isChecked():
            self.sm.setSetting('city_type', 'cus')
        
        self.sm.setSetting('city', self.ui_city_input.text())

        if self.sm.getSetting('city_type') == 'cus' and not self.sm.getSetting('city'):
            QMessageBox.critical(self, "提示", "请重新输入城市名称")
            self.setVisible(True)

        self.sm.saveSetting()

        self.refresh_window.emit()