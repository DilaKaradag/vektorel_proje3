import sys
import googletrans
import language
from PyQt6.QtWidgets import *

class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dila's Translate App(TR-ENG)")
        self.arayuz()

    def arayuz(self):
        ana_widget = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Hangisini kullanacaksınız?"))

        uygulama1 = QPushButton("Türkçeden İngilizceye")
        uygulama1.clicked.connect(self.uygulama1Tiklanma)
        layout.addWidget(uygulama1)

        uygulama2 = QPushButton("İngilizceden Türkçeye")
        uygulama2.clicked.connect(self.uygulama2Tiklanma)
        layout.addWidget(uygulama2)

        ana_widget.setLayout(layout)
        self.setCentralWidget(ana_widget)

    def uygulama1Tiklanma(self):
        central_widget = QWidget()
        layout1 = QVBoxLayout()
        
        
        label_kelime1 = QLabel("Kelimeyi giriniz(TR): ")
        self.kelime1_input = QLineEdit()
        layout.addWidget(label_kelime1)
        layout.addWidget(self.kelime1_input)

        ceviri_button = QPushButton("Çeviri yap")
        ceviri_button.clicked.connect(self.mesaj)
        layout1.addWidget(ceviri_button)

        label_kelime2 = QLabel("Sonuç(ENG): ")
        self.kelime2_input = QLineEdit()
        layout1.addWidget(label_kelime2)
        layout1.addWidget(self.kelime2_input)

        central_widget.setLayout(layout1)
        self.setCentralWidget(central_widget)

def main():
        app= QApplication(sys.argv)
        window = cevirmeEkrani()
        QMessageBox.information(window, "TR-ENG Sözlük", "Sözlük uygulamasına hoş geldiniz.")
        window.show()
        sys.exit(app.exec())