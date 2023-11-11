# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table_item.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QWidget)
import img_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(320, 226)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 10, 0, 10)
        self.ui_wind_label = QLabel(self.frame)
        self.ui_wind_label.setObjectName(u"ui_wind_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_wind_label.sizePolicy().hasHeightForWidth())
        self.ui_wind_label.setSizePolicy(sizePolicy)
        self.ui_wind_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ui_wind_label, 5, 0, 1, 2)

        self.ui_temp_label = QLabel(self.frame)
        self.ui_temp_label.setObjectName(u"ui_temp_label")
        sizePolicy.setHeightForWidth(self.ui_temp_label.sizePolicy().hasHeightForWidth())
        self.ui_temp_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        self.ui_temp_label.setFont(font)
        self.ui_temp_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ui_temp_label, 3, 0, 1, 2)

        self.ui_night_img = QLabel(self.frame)
        self.ui_night_img.setObjectName(u"ui_night_img")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ui_night_img.sizePolicy().hasHeightForWidth())
        self.ui_night_img.setSizePolicy(sizePolicy1)
        self.ui_night_img.setPixmap(QPixmap(u":/img/img/11@2x.png"))
        self.ui_night_img.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ui_night_img, 1, 1, 1, 1)

        self.ui_time_label = QLabel(self.frame)
        self.ui_time_label.setObjectName(u"ui_time_label")
        sizePolicy.setHeightForWidth(self.ui_time_label.sizePolicy().hasHeightForWidth())
        self.ui_time_label.setSizePolicy(sizePolicy)
        self.ui_time_label.setFont(font)
        self.ui_time_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.ui_time_label, 0, 0, 1, 2)

        self.ui_day_img = QLabel(self.frame)
        self.ui_day_img.setObjectName(u"ui_day_img")
        sizePolicy1.setHeightForWidth(self.ui_day_img.sizePolicy().hasHeightForWidth())
        self.ui_day_img.setSizePolicy(sizePolicy1)
        self.ui_day_img.setPixmap(QPixmap(u":/img/img/0@2x.png"))
        self.ui_day_img.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ui_day_img, 1, 0, 1, 1)

        self.ui_day_label = QLabel(self.frame)
        self.ui_day_label.setObjectName(u"ui_day_label")
        sizePolicy.setHeightForWidth(self.ui_day_label.sizePolicy().hasHeightForWidth())
        self.ui_day_label.setSizePolicy(sizePolicy)
        self.ui_day_label.setFont(font)
        self.ui_day_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ui_day_label, 2, 0, 1, 1)

        self.ui_night_lable = QLabel(self.frame)
        self.ui_night_lable.setObjectName(u"ui_night_lable")
        sizePolicy.setHeightForWidth(self.ui_night_lable.sizePolicy().hasHeightForWidth())
        self.ui_night_lable.setSizePolicy(sizePolicy)
        self.ui_night_lable.setFont(font)
        self.ui_night_lable.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ui_night_lable, 2, 1, 1, 1)

        self.ui_hum_label = QLabel(self.frame)
        self.ui_hum_label.setObjectName(u"ui_hum_label")
        sizePolicy.setHeightForWidth(self.ui_hum_label.sizePolicy().hasHeightForWidth())
        self.ui_hum_label.setSizePolicy(sizePolicy)
        self.ui_hum_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ui_hum_label, 4, 0, 1, 2)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ui_wind_label.setText(QCoreApplication.translate("Form", u"\u897f\u5357\u98ce 2\u7ea7\u98ce 45km/h ", None))
        self.ui_temp_label.setText(QCoreApplication.translate("Form", u"23\u00b0C - 18\u00b0C", None))
        self.ui_night_img.setText("")
        self.ui_time_label.setText(QCoreApplication.translate("Form", u"10\u670810\u65e5", None))
        self.ui_day_img.setText("")
        self.ui_day_label.setText(QCoreApplication.translate("Form", u"\u6674", None))
        self.ui_night_lable.setText(QCoreApplication.translate("Form", u"\u96f7\u9635\u96e8", None))
        self.ui_hum_label.setText(QCoreApplication.translate("Form", u"\u76f8\u5bf9\u6e7f\u5ea6 80%", None))
    # retranslateUi

