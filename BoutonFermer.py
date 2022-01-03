from Bouton import Bouton
import sys 
class BoutonFermer(Bouton):
    def __init__(self,parent,position,label):
        super().__init__(parent,position,label)
        self.parent = parent
        self.clicked.connect(self.fermer)
    def fermer(self):
        sys.exit()
      