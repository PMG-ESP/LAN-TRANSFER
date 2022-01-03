

from PyQt5.QtCore import QThread
from Bouton import Bouton
from MessageBox import MessageBox
from ErreurBox import ErreurBox
from PyQt5.QtWidgets import QFileDialog,QInputDialog
import socket
import os
import time

class BoutonEnvoi(Bouton):
    
    def __init__(self,parent,position,label):
        super().__init__(parent,position,label)
        self.parent = parent
        self.clicked.connect(self.envoyer)

    #--Choisir un fichier--
    def choisirFichier(self):
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self.parent,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if filename:
            return filename
    
    #--Saisi de l'adresse Ip--
    def saisirIp(self):
        
        Ip,ok = QInputDialog.getText(self.parent,'Ip','Saisir IP du serveur')
        if ok:
            return Ip

    #--Verification de l'adresse IP--      
    def validerIP(self,s):
        a = s.split('.')
        if len(a) != 4:
            return False
        for x in a:
            if not x.isdigit():
                return False
            i = int(x)
            if i < 0 or i > 255:
                return False
        return True
    
    def preEnvoie(self):
        #--Verifions si l'utilisateur a bien choisi un fichier--

        while True:
            try:
                filename = self.choisirFichier()
                filesize = os.path.getsize(filename)
            except:
                message = MessageBox(self.parent,"Veuillez Choisir un fichier")
                message.click()
            else:
                break
            
        
        time.sleep(0.7)


        host=self.saisirIp()
        while True:
            if host is None:
                messageIp = MessageBox(self.parent,"Veuillez saisir une adresse")
                messageIp.click()
                host=self.saisirIp()
            if self.validerIP(host):
                break   #legal')
            else:
                messageIp = MessageBox(self.parent,"Adresse invalide")
                messageIp.click()
                host=self.saisirIp()


        ####################Envoie du fichier############################
        SEPARATOR = "||||||"
        BUFFER_SIZE = 4096 #envoyer 4096 octets each time step
        port = 5001
       
        #Creation Socket TCP

        try:
            time.sleep(5)
            s = socket.socket()
            s.connect((host,port))
        except:
            messageConnect = ErreurBox(self.parent,"La Connexion a echouée")
            messageConnect.click()
        else:
            #envoi info fichier

            s.send(f"{filename}{SEPARATOR}{filesize}".encode())
            
          #  self.parent.pbar.setRange(0,int(filesize/1024))

            # sending = ProcessusEnvoi(self.parent,s,filename,filesize,BUFFER_SIZE)
            # process = multiprocessing.Process(target=sending.envoi())
            # process.start()
            
            with open(filename, "rb") as f:
                #self.parent.pbar.startPbar()
                inc = 0
                while True:
                    lecture = f.read(BUFFER_SIZE)
                    if not lecture:
                        print("Transfert terminé")
                        break
                    s.sendall(lecture)
                    inc+=int(BUFFER_SIZE/1024)
                   # self.parent.pbar.setPvalue(inc)  
           # self.parent.pbar.setValue(int(filesize/1024))
            s.close()
            time.sleep(1.5)
            self.parent.message.click()

    def envoyer(self):
        t = MyThread(target=self.preEnvoie())
        t.start()
        t.quit()



class MyThread(QThread):
    def __init__(self, target=None):
        super().__init__()
        self.target = target
    
    def run(self):
        if self.target:
            self.target()


