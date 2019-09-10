from terminal.caesar import caesar_get_error, caesar_main
from terminal.vigenère import vigenere_get_error, vigenere_main
from PyQt5.QtWidgets import (QApplication, QComboBox, QMainWindow, QMessageBox, QPlainTextEdit, QPushButton)
import sys


class MainWindow(QMainWindow):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.resize(640, 480)
        self.setWindowTitle("Ciphers")

        self.userText = QPlainTextEdit(self)
        self.userText.setPlaceholderText("Input...")
        self.userText.move(10, 10)
        self.userText.resize(250, 460)

        self.changedText = QPlainTextEdit(self)
        self.changedText.setReadOnly(True)
        self.changedText.setPlaceholderText("Output")
        self.changedText.move(380, 10)
        self.changedText.resize(250, 460)

        self.cipherBox = QComboBox(self)
        self.cipherBox.addItems(["Caesar", "Vigenere"])
        self.cipherBox.move(270, 25)

        self.modeBox = QComboBox(self)
        self.modeBox.addItems(["Cipher", "Decipher"])
        self.modeBox.move(270, 100)

        self.keyText = QPlainTextEdit(self)
        self.keyText.setPlaceholderText("Key...")
        self.keyText.resize(100, 60)
        self.keyText.move(270, 175)

        self.cipherButton = QPushButton("GO", self)
        self.cipherButton.resize(100, 60)
        self.cipherButton.move(270, 250)
        self.cipherButton.clicked.connect(self.cipher)

        self.swapButton = QPushButton("<-- Swap -->", self)
        self.swapButton.move(270, 325)
        self.swapButton.clicked.connect(self.swap)

        self.clearButton = QPushButton("Clear", self)
        self.clearButton.move(270, 375)
        self.clearButton.clicked.connect(self.clear)

    def cipher(self):
        if self.cipherBox.currentText() == "Caesar":
            error, user_key = caesar_get_error(self.keyText.toPlainText())
            if len(error) == 0:
                self.changedText.setPlainText(caesar_main(self.userText.toPlainText(), user_key, self.modeBox.currentText()))
            else:
                QMessageBox.critical(None, "An exception was raised", error)
        if self.cipherBox.currentText() == "Vigenere":
            error = vigenere_get_error(self.keyText.toPlainText())
            if len(error) == 0:
                self.changedText.setPlainText(vigenere_main(self.userText.toPlainText(), self.keyText.toPlainText(), self.modeBox.currentText()))
            else:
                QMessageBox.critical(None, "An exception was raised", error)

    def swap(self):
        holder = self.userText.toPlainText()
        self.userText.setPlainText(self.changedText.toPlainText())
        self.changedText.setPlainText(holder)

    def clear(self):
        self.userText.setPlainText("")
        self.changedText.setPlainText("")


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