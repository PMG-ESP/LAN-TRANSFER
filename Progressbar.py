from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class Progressbar(QProgressBar):

    def __init__(self,parent,position,max):
        super().__init__(parent)
        self.parent = parent
        self.setGeometry(position[0],position[1],position[2],position[3])
        self.setRange(0,max)
    
    def design(self):
        self.setStyleSheet("color:#00111c;background-color: #0096c7 ;border-width: : 2px;border-radius: : 10px;")
        self.setAlignment(Qt.AlignCenter)

