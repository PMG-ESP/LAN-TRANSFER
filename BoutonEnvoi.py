from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from APK.Bouton import Bouton
import socket
import os
import time
class BoutonEnvoi(Bouton):
    
    def __init__(self,parent,position,label):
        super().__init__(parent,position,label)
        self.parent = parent
        self.clicked.connect(self.envoyer)

    
    def choisirFichier(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self.parent,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            return fileName
    def saisirIp(self):
        global Ip
        Ip,ok = QInputDialog.getText(self.parent,'Ip','Saisir IP du serveur')
        if ok:
            return Ip

    def envoyer(self):
        filename = self.choisirFichier()
        time.sleep(0.7)
        self.saisirIp()

        ####################Envoie du fichier############################
        SEPARATOR = "||||||"
        BUFFER_SIZE = 4096 #envoyer 4096 octets each time step
        host = Ip
        port = 5001
        filesize = os.path.getsize(filename)
    
        #Creation Socket TCP
        s = socket.socket()
        s.connect((host,port))
        #envoi info fichier

        s.send(f"{filename}{SEPARATOR}{filesize}".encode())
        
        self.parent.pbar.setRange(0,filesize)

        with open(filename, "rb") as f:
            inc = 0
            while True:
                lecture = f.read(BUFFER_SIZE)
                if not lecture:
                    print("Transfert terminé")
                    break
                s.sendall(lecture)
                inc+=BUFFER_SIZE
                self.parent.pbar.setValue(inc)  
        self.parent.pbar.setValue(filesize)
        s.close()