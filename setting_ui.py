# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QGroupBox, QLineEdit, QRadioButton,
    QSizePolicy, QWidget)

class Ui_Setting(object):
    def setupUi(self, Setting):
        if not Setting.objectName():
            Setting.setObjectName(u"Setting")
        Setting.resize(250, 150)
        self.gridLayout = QGridLayout(Setting)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(Setting)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ui_radio_cus = QRadioButton(self.groupBox_2)
        self.ui_radio_cus.setObjectName(u"ui_radio_cus")

        self.gridLayout_2.addWidget(self.ui_radio_cus, 1, 0, 1, 1)

        self.ui_city_input = QLineEdit(self.groupBox_2)
        self.ui_city_input.setObjectName(u"ui_city_input")

        self.gridLayout_2.addWidget(self.ui_city_input, 1, 1, 1, 1)

        self.ui_radio_curr = QRadioButton(self.groupBox_2)
        self.ui_radio_curr.setObjectName(u"ui_radio_curr")
        self.ui_radio_curr.setChecked(True)

        self.gridLayout_2.addWidget(self.ui_radio_curr, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Setting)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(Setting)
        self.buttonBox.accepted.connect(Setting.accept)
        self.buttonBox.rejected.connect(Setting.reject)

        QMetaObject.connectSlotsByName(Setting)
    # setupUi

    def retranslateUi(self, Setting):
        Setting.setWindowTitle(QCoreApplication.translate("Setting", u"\u8bbe\u7f6e", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Setting", u"\u9ed8\u8ba4\u57ce\u5e02", None))
        self.ui_radio_cus.setText(QCoreApplication.translate("Setting", u"\u81ea\u5b9a\u4e49", None))
        self.ui_radio_curr.setText(QCoreApplication.translate("Setting", u"\u5f53\u524d\u57ce\u5e02", None))
    # retranslateUi

