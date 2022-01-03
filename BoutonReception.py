import multiprocessing

from PyQt5.QtCore import QThread
from Bouton import Bouton
import socket
import time
import os
class BoutonReception(Bouton):
    def __init__(self,parent,position,label):
        super().__init__(parent,position,label)
        self.parent = parent
        self.clicked.connect(self.recevoir)
    
    def preRecep(self):
        server_addr = "0.0.0.0"
        server_port = 5001
        BUFFER_SIZE = 4096
        SEPARATOR = "||||||"

        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((server_addr,server_port))
        s.listen(5)

        client_socket, address = s.accept() #Le client est connecte

        received = client_socket.recv(BUFFER_SIZE).decode()
        filename ,filesiz = received.split(SEPARATOR)
        filename = os.path.basename(filename)

        filesize = int(filesiz)
        self.parent.pbar.setRange(0,int(filesize/1024))

        with open(filename, "wb") as f:
            inc= 0
            while True:
                lecture = client_socket.recv(BUFFER_SIZE)
                if not lecture:
                    print("transfert terminé")
                    break
                f.write(lecture)
                inc+=int(BUFFER_SIZE/1024)
                self.parent.pbar.setValue(inc)
        self.parent.pbar.setValue(int(filesize/1024))
        client_socket.close()
        s.close()
        time.sleep(1.5)
        self.parent.message.click()
    def recevoir(self):
        t = MyThread(target=self.preRecep())
        t.start()        

class MyThread(QThread):
    def __init__(self, target=None):
        super().__init__()
        self.target = target
    
    def run(self):
        if self.target:
            self.target()