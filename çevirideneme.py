import googletrans
import sys
import language
import masaüstü
from PyQt6.QtWidgets import *


class cevirmeEkrani(QMainWindow):
        def oturum(self):
                kullaniciadi = input("Kullanıcı adınızı giriniz: ")
                sifre = input("Şifrenizi giriniz: ")

                if kullaniciadi == "dila" and sifre == "12345":
                        print("Uygulamaya hoş geldiniz.")
                else:
                        print("Hatalı giriş yaptınız. Lütfen kontrol ediniz.")
        
        
        
        def __init__(self):
                super().__init__()

                self.setWindowTitle("TR-ENG SÖZLÜK")
                self.arayuz()

        def arayuz(self):
                central_widget = QWidget()
                layout = QVBoxLayout()

                label_kelime1 = QLabel("İlk kelimeyi giriniz: ")
                self.kelime1_input = QLineEdit()
                layout.addWidget(label_kelime1)
                layout.addWidget(self.kelime1_input)

                label_kelime2 = QLabel()
                self.kelime2_input = QLineEdit()
                layout.addWidget(label_kelime2)
                layout.addWidget(self.kelime2_input)

                ceviri_button = QPushButton("Çeviri yap.")
                ceviri_button.clicked.connect(self.mesaj)
                layout.addWidget(ceviri_button)

                central_widget.setLayout(layout)
                self.setCentralWidget(central_widget)

        def mesaj(self):
                kelime1 = int(self.kelime1_input.text()) * 2
                self.kelime2_input.setText(str(kelime1))

def main():
        app= QApplication(sys.argv)
        window = cevirmeEkrani()
        QMessageBox.information(window, "TR-ENG Sözlük", "Sözlük uygulamasına hoş geldiniz.")
        window.show()
        sys.exit(app.exec())

if __name__ == "__main__":
        main()