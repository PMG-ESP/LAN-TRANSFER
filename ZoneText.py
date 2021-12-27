from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import socket
class ZoneText(QLabel):
    def __init__(self,parent,position,text):
        super().__init__(parent)
        self.parent = parent
        self.setText(text)
        self.setGeometry(position[0],position[1],position[2],position[3])
    
    def getIP(self):
        st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:       
            st.connect(('10.255.255.255', 1))
            IP = st.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            st.close()
        self.setText(f"Addresse IP: {IP} ")
