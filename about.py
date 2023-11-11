import json
from PySide6.QtWidgets import QDialog
from about_ui import Ui_About

class AboutWindow(QDialog, Ui_About):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
