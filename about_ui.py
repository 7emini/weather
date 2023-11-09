# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)
import image_rc
import image_rc

class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName(u"About")
        About.resize(223, 133)
        self.verticalLayout = QVBoxLayout(About)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(About)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/weather/resource/image/weather_s.png"))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(About)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(About)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(8)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"\u5173\u4e8e", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("About", u"\u5929\u6c14 v1.0", None))
        self.label_3.setText(QCoreApplication.translate("About", u"by Gemin", None))
    # retranslateUi

