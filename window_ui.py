# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QLabel,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QVBoxLayout,
    QWidget)
import img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(405, 500)
        icon = QIcon()
        icon.addFile(u":/img/img/weather.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionCity = QAction(MainWindow)
        self.actionCity.setObjectName(u"actionCity")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionRefresh = QAction(MainWindow)
        self.actionRefresh.setObjectName(u"actionRefresh")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{background-color:#fff}\n"
"#ui_city_label{color:#696969}")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, -1, 10, -1)
        self.ui_day_img = QLabel(self.centralwidget)
        self.ui_day_img.setObjectName(u"ui_day_img")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_day_img.sizePolicy().hasHeightForWidth())
        self.ui_day_img.setSizePolicy(sizePolicy)
        self.ui_day_img.setPixmap(QPixmap(u":/img/img/0@2x.png"))
        self.ui_day_img.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.ui_day_img)

        self.ui_day_label = QLabel(self.centralwidget)
        self.ui_day_label.setObjectName(u"ui_day_label")
        font = QFont()
        font.setPointSize(24)
        self.ui_day_label.setFont(font)
        self.ui_day_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.ui_day_label)

        self.ui_city_label = QLabel(self.centralwidget)
        self.ui_city_label.setObjectName(u"ui_city_label")
        self.ui_city_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.ui_city_label)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy1)
        self.listWidget.setFrameShape(QFrame.NoFrame)
        self.listWidget.setFrameShadow(QFrame.Plain)
        self.listWidget.setLineWidth(0)
        self.listWidget.setAutoScroll(True)
        self.listWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.listWidget.setResizeMode(QListView.Adjust)

        self.verticalLayout_2.addWidget(self.listWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 405, 24))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionCity)
        self.menu.addAction(self.actionAbout)
        self.menu.addAction(self.actionRefresh)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5929\u6c14", None))
        self.actionCity.setText(QCoreApplication.translate("MainWindow", u"\u57ce\u5e02", None))
#if QT_CONFIG(shortcut)
        self.actionCity.setShortcut(QCoreApplication.translate("MainWindow", u"Meta+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
#if QT_CONFIG(shortcut)
        self.actionAbout.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionRefresh.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
#if QT_CONFIG(shortcut)
        self.actionRefresh.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.ui_day_img.setText("")
        self.ui_day_label.setText(QCoreApplication.translate("MainWindow", u"\u6674 12\u00b0C", None))
        self.ui_city_label.setText(QCoreApplication.translate("MainWindow", u"\u4e1c\u8425", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
    # retranslateUi

