from PyQt5.QtCore import QThread,pyqtSignal

class PbarThread(QThread):

    changeValue = pyqtSignal(int)

    def run(self):
        self.changeValue.emit(int)