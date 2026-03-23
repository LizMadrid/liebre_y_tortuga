
from PyQt6.QtWidgets import QWidget, QPushButton, QLabel
from PyQt6.QtGui import QPixmap
from sub_process import SubProceso

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Liebre vs Tortuga")
        self.setGeometry(100, 100, 800, 400)

        #Imagen Liebre
        self.imgLiebre = QLabel(self)
        self.imgLiebre.setPixmap(QPixmap("./img/liebre.png"))
        self.imgLiebre.setScaledContents(True)
        self.imgLiebre.resize(100, 100)
        self.imgLiebre.move(10,50)

        #Imagen Tortuga
        