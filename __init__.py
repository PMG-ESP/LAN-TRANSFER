import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from APK.FenetrePrincipale import FenetrePrincipale
from APK.Bouton import Bouton
from APK.BoutonEnvoi import BoutonEnvoi
from APK.BoutonReception import BoutonReception
from APK.BoutonFermer import BoutonFermer
from APK.Progressbar import Progressbar
from APK.ZoneText import ZoneText

app = QApplication(sys.argv)

#position = (gaucheDecal,hautDecal,largeur,hauteur)
dim = (400,200,320,480)                         #--positions de la fenetre principale--
win = FenetrePrincipale("LAN-TRANSFER",dim)
win.design()
pos1 = (30,330,100,50)  #--bouton envoi--
pos2 = (190,330,100,50) #--bouton reception--
pos3 = (90,400,130,50)  #--bouton fermer--

boutonSend = BoutonEnvoi(win,pos1,'Envoyer')
boutonSend.design()

boutonRecv = BoutonReception(win,pos2,'Recevoir')
boutonRecv.design()

boutonquit = BoutonFermer(win,pos3,'Fermer')
boutonquit.design()

posText = (10,50,200,50)
text1 = ZoneText(win,posText,"")
text1.getIP()

win.show()
app.exec_()