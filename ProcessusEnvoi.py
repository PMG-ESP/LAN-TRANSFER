import time
class ProcessusEnvoi():
    def __init__(self,parent,socket,filename,filesize,BUFFER_SIZE):
        self.socket = socket
        self.filesize = filesize
        self.parent = parent
        self.filename = filename
        self.BUFFER_SIZE = BUFFER_SIZE

    def envoi(self):
        with open(self.filename, "rb") as f:
            inc = 0
            while True:
                lecture = f.read(self.BUFFER_SIZE)
                if not lecture:
                    print("Transfert terminé")
                    break
                self.socket.sendall(lecture)
                inc+=int(self.BUFFER_SIZE/1024)
                self.parent.pbar.setValue(inc)
            self.parent.pbar.setValue(int(self.filesize/1024))
            self.socket.close()
            time.sleep(1.5)
            self.parent.message.click()
        