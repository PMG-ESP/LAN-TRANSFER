
from PyQt5.QtWidgets import QWidget
from MessageBox import MessageBox
from Progressbar import Progressbar
from BoutonEnvoi import BoutonEnvoi
from BoutonReception import BoutonReception
from BoutonFermer import BoutonFermer
from ZoneText import ZoneText

class FenetrePrincipale(QWidget):

    
    #--Constructeur--
    def __init__(self,titre,position):
        #position = (gaucheDecal,hautDecal,largeur,hauteur)
        
        super().__init__()

        #--dimensions de le fenetre principale--
        self.setWindowTitle("LAN-TRANFER")
        self.setGeometry(position[0],position[1],position[2],position[3])

        #--Contenu de la fenetre principale--
        
        pos1 = (30,330,100,50)  #--position du bouton envoi--
        pos2 = (190,330,100,50) #--position du bouton reception--
        pos3 = (90,400,130,50)  #--position du bouton fermer--

        boutonSend = BoutonEnvoi(self,pos1,'Envoyer')
        boutonSend.design()

        boutonRecv = BoutonReception(self,pos2,'Recevoir')
        boutonRecv.design()

        boutonquit = BoutonFermer(self,pos3,'Fermer')
        boutonquit.design()

        posText = (10,50,200,50)
        text1 = ZoneText(self,posText,"")
        text1.getIP()
        text1.design
        #--progressbar--
        posPbar = (35,200,250,20) #--positions progressbar--

        self.pbar = Progressbar(self,posPbar,100)
        self.pbar.design()

        self.message  = MessageBox(self," Transfert Terminé ")
        self.message.design()
    
    def design(self):
        self.setStyleSheet("color:#0096c7;background-color: #00111c ;border-width: : 2px;border-radius: : 10px;")
    
