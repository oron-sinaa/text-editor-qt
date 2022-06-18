import sys, os

from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog)
from PyQt5.QtGui import QFontDatabase
from PyQt5 import QtGui

from PyQt5.uic import loadUi

from ui_main import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # path is none until file is open or saved
        self.path = None
        # TODO: shift to UI later
        self.setWindowTitle("Untitled - QtPad")
        self.setWindowIcon(QtGui.QIcon("ui\\resources\\icon.png"))
        self.editor = self.ui.textEdit
        # setting default font
        fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedfont.setPointSize(12)
        self.editor.setFont(fixedfont)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.ui.action_Open.triggered.connect(self.file_open)
        self.ui.actionSave.triggered.connect(self.file_save)
        self.ui.actionCut.triggered.connect(self.editor.cut)
        self.ui.actionCopy.triggered.connect(self.editor.copy)
        self.ui.actionPaste.triggered.connect(self.editor.paste)
        self.ui.actionUndo.triggered.connect(self.editor.undo)
        self.ui.actionRedo.triggered.connect(self.editor.redo)

    def file_open(self):
        # getting path and bool value
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.txt);All files (*.*)")
        if path:
            try:
                with open(path, "rU") as f:
                    text = f.read()
            except Exception as e:
                self.dialog_critical(str(e))
            else:
                self.path = path
                # add text from file to text editor widget
                self.editor.setPlainText(text)
                # self.update_title()

    def file_save(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())