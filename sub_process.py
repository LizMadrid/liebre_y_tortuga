import time
from PyQt6.QtCore import QThread, pyqtSignal




class SubProceso(QThread):
    actualizar = pyqtSignal(int, int)

    def __init__(self, label, tiempo):
        super().__init__()
        self.label= label
        self.tiempo= tiempo

    def run(self):
        while True:
            x=self.label.x()
            y=self.label.y()

            if x < 550:
                x += 10
            else:
                y += 10

            self.actualizar.emit(x,y)
            time.sleep(self.tiempo / 1000.0)        