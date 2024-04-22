from PyQt6.QtWidgets import * 
import sys

class secimEkrani(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seçiniz:")

    def arayuz(self):

        yerlesimY1 = QHBoxLayout()
        yerlesimD1 = QVBoxLayout()
        yerlesimD2 = QVBoxLayout()

        bilgi1 = QLabel("Türkçeden İngilizceye çeviri")
        bilgi2 = QLabel("İngilizceden Türkçeye çeviri")
        yerlesimD1.addWidget(bilgi1)
        yerlesimD1.addWidget(bilgi2)

        buton1 = QPushButton("Buton 1")
        buton2 = QPushButton("Buton 2")
        yerlesimD2.addWidget(buton1)
        yerlesimD2.addWidget(buton2)
        
        araclar = QWidget()
        araclar.setLayout()
        self.setCentralWidget(araclar)

        

uygulama = QApplication([])
pencere = secimEkrani()
pencere.show()
uygulama.exec()


