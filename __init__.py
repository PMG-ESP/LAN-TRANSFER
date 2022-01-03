import sys
from PyQt5.QtWidgets import QApplication
from FenetrePrincipale import FenetrePrincipale


def main():
    QApplication.setStyle('Fusion')
    app = QApplication(sys.argv)
    #position = (gaucheDecal,hautDecal,largeur,hauteur)
    dim = (400,200,320,480)                         #--positions de la fenetre principale--
    win = FenetrePrincipale("LAN-TRANSFER",dim)
    win.design()
    
    
    win.show()
    sys.exit(app.exec_())


main()