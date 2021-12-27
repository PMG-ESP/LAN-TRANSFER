from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from APK.Progressbar import Progressbar
class FenetrePrincipale(QWidget):

    
    
    #--Constructeur--
    def __init__(self,titre,position):

        #position = (gaucheDecal,hautDecal,largeur,hauteur)

        super().__init__()
        self.setWindowTitle("LAN-TRANFER")
        self.setGeometry(position[0],position[1],position[2],position[3])

        #--progressbar--
        posPbar = (50,100,200,50) #--positions progressbar--

        self.pbar = Progressbar(self,posPbar,100)
        self.pbar.design()
    
    def design(self):
        self.setStyleSheet("color:#0096c7;background-color: #00111c ;border-width: : 2px;border-radius: : 10px;")
