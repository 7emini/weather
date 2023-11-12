import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from window import Window
# import qtvscodestyle as qtvsc



if __name__ == '__main__':
    app = QApplication()
    win = Window()

    # main_win.setCentralWidget(push_button)

    # stylesheet = qtvsc.load_stylesheet(qtvsc.Theme.LIGHT_VS)
    # stylesheet = load_stylesheet(qtvsc.Theme.LIGHT_VS)
    # app.setStyleSheet(stylesheet)

    win.show()

    
    sys.exit(app.exec())