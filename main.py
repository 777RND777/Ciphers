from cipher.caesar import caesar_get_error, caesar_main
from cipher.vigenère import vigenere_get_error, vigenere_main
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QFileDialog,
                             QMainWindow, QMessageBox, QPlainTextEdit, QPushButton)
import os
import sys


class MainWindow(QMainWindow):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.resize(1080, 640)
        self.setWindowTitle("Ciphers")

        self.inputText = QPlainTextEdit()
        self.inputText.setPlaceholderText("Input...")
        self.inputText.move(10, 10)
        self.inputText.resize(400, 620)

        self.outputText = QPlainTextEdit()
        self.outputText.setReadOnly(True)
        self.outputText.setPlaceholderText("Output")
        self.outputText.move(670, 10)
        self.outputText.resize(400, 620)

        self.userTextButton = QPushButton("File")
        self.userTextButton.move(420, 20)
        self.userTextButton.clicked.connect(self.open_file)

        self.changedTextButton = QPushButton("Save")
        self.changedTextButton.move(560, 20)
        self.changedTextButton.clicked.connect(self.save_file)

        self.cipherBox = QComboBox()
        self.cipherBox.addItems(["Caesar", "Vigenere"])
        self.cipherBox.move(420, 70)

        self.modeBox = QComboBox()
        self.modeBox.addItems(["Cipher", "Decipher"])
        self.modeBox.move(560, 70)

        self.keyText = QPlainTextEdit()
        self.keyText.setPlaceholderText("Key...")
        self.keyText.resize(100, 60)
        self.keyText.move(420, 120)

        self.cipherButton = QPushButton("GO")
        self.cipherButton.resize(100, 60)
        self.cipherButton.move(560, 120)
        self.cipherButton.clicked.connect(self.cipher)

        self.swapButton = QPushButton("<-- Swap -->")
        self.swapButton.move(420, 200)
        self.swapButton.clicked.connect(self.swap)

        self.clearButton = QPushButton("Clear")
        self.clearButton.move(560, 200)
        self.clearButton.clicked.connect(self.clear)

        self.clearCheckKey = QCheckBox("key")
        self.clearCheckKey.setChecked(True)
        self.clearCheckKey.move(585, 225)

    def cipher(self):
        if self.cipherBox.currentText() == "Caesar":
            error, user_key = caesar_get_error(self.keyText.toPlainText())
            if len(error) == 0:
                self.outputText.setPlainText(caesar_main(self.inputText.toPlainText(), user_key, self.modeBox.currentText()))
            else:
                QMessageBox.critical(None, "An exception was raised", error)
        if self.cipherBox.currentText() == "Vigenere":
            error = vigenere_get_error(self.keyText.toPlainText())
            if len(error) == 0:
                self.outputText.setPlainText(vigenere_main(self.inputText.toPlainText(), self.keyText.toPlainText(), self.modeBox.currentText()))
            else:
                QMessageBox.critical(None, "An exception was raised", error)

    def swap(self):
        holder = self.inputText.toPlainText()
        self.inputText.setPlainText(self.outputText.toPlainText())
        self.outputText.setPlainText(holder)

    def clear(self):
        self.inputText.setPlainText("")
        self.outputText.setPlainText("")
        if self.clearCheckKey.isChecked():
            self.keyText.setPlainText("")

    def open_file(self):
        file = QFileDialog.getOpenFileName(None, 'Open file', os.path.dirname(os.path.abspath(__file__)), "*.txt")[0]
        try:
            with open(file, 'r') as f:
                self.inputText.setPlainText(f.read())
        except FileNotFoundError:
            pass

    def save_file(self):
        file = QFileDialog.getSaveFileName(None, 'Save file', os.path.dirname(os.path.abspath(__file__)), "*.txt")[0]
        with open(file, 'w') as f:
            f.write(self.outputText.toPlainText())


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
