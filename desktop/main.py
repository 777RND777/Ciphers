from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QComboBox, QMessageBox, QPlainTextEdit)
import sys


class MainWindow(QMainWindow):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        width = 640
        height = 480
        padding = 10
        self.resize(width, height)

        self.userText = QPlainTextEdit(self)
        self.userText.move(padding, padding)
        self.userText.resize((width - self.cipherBox.size().width()) / 2 - padding * 2, height - padding * 2)

        self.cipherBox = QComboBox(self)
        self.cipherBox.addItems(["Caesar", "Vigenere"])
        self.cipherBox.move((width - self.cipherBox.size().width()) / 2, (height - self.cipherBox.size().height()) / 2)




def catch_exceptions(t, val, tb):
    QMessageBox.critical(None, 'An exception was raised', 'Exception type: {}'.format(t))
    old_hook(t, val, tb)


if __name__ == '__main__':
    old_hook = sys.excepthook
    sys.excepthook = catch_exceptions

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())