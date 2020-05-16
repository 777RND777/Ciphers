from cipher.caesar import caesar_get_error, caesar_main
from cipher.vigenère import vigenere_get_error, vigenere_main
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QFileDialog, QHBoxLayout,
                             QMessageBox, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget)
import os
import sys


class MainWindow(QWidget):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.resize(1080, 640)
        self.setWindowTitle("Ciphers")

        self.inputText = QPlainTextEdit()
        self.inputText.setPlaceholderText("Input...")

        self.outputText = QPlainTextEdit()
        self.outputText.setReadOnly(True)
        self.outputText.setPlaceholderText("Output")

        self.openFileButton = QPushButton("File")
        self.openFileButton.clicked.connect(self.open_file)

        self.saveFileButton = QPushButton("Save")
        self.saveFileButton.clicked.connect(self.save_file)

        self.cipherBox = QComboBox()
        self.cipherBox.addItems(["Caesar", "Vigenere"])

        self.modeBox = QComboBox()
        self.modeBox.addItems(["Cipher", "Decipher"])

        self.keyText = QPlainTextEdit()
        self.keyText.setPlaceholderText("Key...")

        self.clearButton = QPushButton("Clear")
        self.clearButton.clicked.connect(self.clear)

        self.clearCheckKey = QCheckBox("key")
        self.clearCheckKey.setChecked(True)

        self.swapButton = QPushButton("<-- Swap -->")
        self.swapButton.clicked.connect(self.swap)

        self.cipherButton = QPushButton("GO")
        self.cipherButton.clicked.connect(self.cipher)

        self.fileLayout = QHBoxLayout()
        self.fileLayout.addWidget(self.openFileButton, alignment=Qt.AlignBaseline)
        self.fileLayout.addWidget(self.saveFileButton, alignment=Qt.AlignBaseline)

        self.cipherLayout = QHBoxLayout()
        self.cipherLayout.addWidget(self.cipherBox, alignment=Qt.AlignBaseline)
        self.cipherLayout.addWidget(self.modeBox, alignment=Qt.AlignBaseline)

        self.commandLayout = QHBoxLayout()
        self.commandLayout.addWidget(self.clearButton, alignment=Qt.AlignBaseline)
        self.commandLayout.addWidget(self.swapButton, alignment=Qt.AlignBaseline)

        self.userLayout = QVBoxLayout()
        self.userLayout.addLayout(self.fileLayout)
        self.userLayout.addLayout(self.cipherLayout)
        self.userLayout.addWidget(self.keyText, alignment=Qt.AlignCenter)
        self.userLayout.addWidget(self.cipherButton, alignment=Qt.AlignBaseline)
        self.userLayout.addLayout(self.commandLayout)
        self.userLayout.addWidget(self.clearCheckKey, alignment=Qt.AlignTop)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.inputText)
        self.mainLayout.addLayout(self.userLayout)
        self.mainLayout.addWidget(self.outputText)

        self.setLayout(self.mainLayout)

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
