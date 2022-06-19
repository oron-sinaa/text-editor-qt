import sys, os

from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox)
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
        # make an instance of textEdit widget for further use
        self.editor = self.ui.textEdit
        # setting default font
        fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedfont.setPointSize(12)
        self.editor.setFont(fixedfont)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.ui.action_Open.triggered.connect(self.file_open)
        self.ui.actionOpen.triggered.connect(self.file_open)
        self.ui.actionSave.triggered.connect(self.file_save)
        self.ui.actionSave_2.triggered.connect(self.file_save)
        self.ui.actionSave_As.triggered.connect(self.file_save_as)
        # TODO: add save as to file menu
        self.ui.actionCut.triggered.connect(self.editor.cut)
        self.ui.actionCut_2.triggered.connect(self.editor.cut)
        self.ui.actionCopy.triggered.connect(self.editor.copy)
        self.ui.actionCopy_2.triggered.connect(self.editor.copy)
        self.ui.actionPaste.triggered.connect(self.editor.paste)
        self.ui.actionPaste_2.triggered.connect(self.editor.paste)
        # TODO: add undo to file menu
        self.ui.actionUndo.triggered.connect(self.editor.undo)
        # TODO: add redo to file menu
        self.ui.actionRedo.triggered.connect(self.editor.redo)
        self.ui.actionExit.triggered.connect(lambda: self.exit_app())

    def file_open(self):
        # getting path and define file type (returns tuple)
        path, file_type = QFileDialog.getOpenFileName(
            self, "Choose a text file", "", "Text Files (*.txt); All files (*.*)"
        )
        if path:
            try:
                with open(path, "r") as f:
                    text = f.read()
                    f.close()
            except Exception as e:
                self.dialog_critical(str(e))
            else:
                self.path = path
                # display the text from file to text editor widget
                self.editor.setPlainText(text)
                self.update_title()

    def file_save(self):
        if self.path is None:
            return self.file_save_as()
        self.save_to_path(self.path)

    def file_save_as(self):
        path, file_type = QFileDialog.getSaveFileName(
            self, "Save as", "",  "Text Files (*.txt)"
        )
        if not path:
            # save as dialog cancelled -> nothing to do
            return
        self.save_to_path(path)

    def save_to_path(self, path):
        text = self.editor.toPlainText()
        # if len(text) > 0:
        try:
            with open(path, 'w+') as f:
                f.write(text)
        except Exception as e:
            self.dialog_critical(str(e))
        else:
            # set new path
            self.path = path
            self.update_title()
        

    def dialog_critical(self, e):
        dlg = QMessageBox(self)
        # setting exception text to the dialog
        dlg.setText(e)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def update_title(self):
        self.setWindowTitle(
            "{} - PyQt5 Notepad".format((os.path.basename(self.path) if self.path else "Untitled"))
        )

    def exit_app(self):
        reply = QMessageBox.question(
            self, 'Exit Editor?', 'Are you sure you want to exit QtPad?', 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
                self.close()
        else:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())