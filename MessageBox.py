from PyQt5.QtWidgets import QMessageBox
import sys


class MessageBox(QMessageBox):
    def __init__(self,parent,text):
        
        super().__init__(parent)
        self.parent = parent
        self.setText(text)
        self.setWindowTitle("ATTENTION")
        
    def design(self):
        self.setStyleSheet("color:#00111c;background-color: #0096c7 ;border-width: : 2px;border-radius: : 10px;")
    
    def click(self):
        ok = self.addButton(QMessageBox.Ok)
        ok.setText("OK")
        close = self.addButton(QMessageBox.Close)
        close.setText("Fermer")
        self.exec_()

        if self.clickedButton() == close:
            sys.exit()
        elif self.clickedButton() == ok:
            pass