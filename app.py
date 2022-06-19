import sys, os

from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox, QLabel)
from PyQt5.QtGui import QFontDatabase
from PyQt5 import QtGui
from PyQt5.uic import loadUi

import qdarktheme

from ui_main import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        app.setStyleSheet(qdarktheme.load_stylesheet("dark"))
        self.ui.setupUi(self)
        self.ui.statusbar.showMessage("{} Words | {} Characters".format(self.get_wordcount(), self.get_charcount()))
        # path is none until file is open or saved
        self.path = None
        self.setWindowTitle("Untitled - QtPad")
        self.setWindowIcon(QtGui.QIcon("ui\\resources\\icon.png"))
        # template for any hyperlink to be used
        self.link_template = "<a href={0}>{1}</a>"
        # make an instance of text Edit widget for further use
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
        self.ui.actionSaveAs_2.triggered.connect(self.file_save_as)
        self.ui.actionCut.triggered.connect(self.editor.cut)
        self.ui.actionCut_2.triggered.connect(self.editor.cut)
        self.ui.actionCopy.triggered.connect(self.editor.copy)
        self.ui.actionCopy_2.triggered.connect(self.editor.copy)
        self.ui.actionPaste.triggered.connect(self.editor.paste)
        self.ui.actionPaste_2.triggered.connect(self.editor.paste)
        self.ui.actionUndo.triggered.connect(self.editor.undo)
        self.ui.actionUndo_2.triggered.connect(self.editor.undo)
        self.ui.actionRedo.triggered.connect(self.editor.redo)
        self.ui.actionRedo_2.triggered.connect(self.editor.redo)
        self.ui.actionDark_Light.triggered.connect(self.set_theme)
        self.ui.actionAbout.triggered.connect(self.show_about_dialog)
        self.ui.actionExit.triggered.connect(self.exit_app)
        # FIXME: Connect to display word and character count on statusbar
        # self.editor.textChanged.connect()

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

    def show_about_dialog(self):
        QMessageBox.about(
            self,
            "About QtPad v1.0",
            "<b>A text editor built using:</b>"
            "<li>- PyQt5</li>"
            "<li>- Qt Designer</li>"
            "<li>- Python</li>"
            "<a href = 'https://github.com/oron-sinaa/text-editor-qt'>github repository</a> 🔗",
        )
    
    def get_wordcount(self):
        return ('?')
        # text = self.ui.textEdit.toPlainText()
        
    def get_charcount(self):
        return ('?')
        # text = self.ui.textEdit.toPlainText()
        # char_count = len(text)
        # return char_count

    def set_theme(self):
        if self.ui.actionDark_Light.isChecked():
            app.setStyleSheet(qdarktheme.load_stylesheet("dark"))
        else:
            app.setStyleSheet(qdarktheme.load_stylesheet("light"))

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