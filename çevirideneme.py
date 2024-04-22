import googletrans
import sys
import language
import masaüstü
from PyQt6.QtWidgets import *


class loginEkrani(QMainWindow):
    def kontrol(self):
        kullaniciadi = self.ka.text()
        sifre = self.sf.text()
        #print("Tıklandı", kadi, sifre)
        if kullaniciadi == "dila" and sifre == "12345":
            print("Giriş yapabilir.")
        else:
            print("Hatalı kullanıcı adı veya şifre!")
        
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")

        icerik = QVBoxLayout() # layout oluşturduk Vertical
#icerik = QHBoxLayout()
        icerik.addWidget(QLabel("Kullanıcı adı: "))
        self.ka = QLineEdit()
        icerik.addWidget(self.ka)
        icerik.addWidget(QLabel("Şifre: "))
        self.sf = QLineEdit()
        icerik.addWidget(self.sf)
        buton1 = QPushButton("Giriş yap")
        icerik.addWidget(buton1)
        icerik.addWidget(QLabel("Sonuç: "))
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

        buton1.clicked.connect(self.kontrol)




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

                label_kelime1 = QLabel("İlk kelimeyi giriniz(TR): ")
                self.kelime1_input = QLineEdit()
                layout.addWidget(label_kelime1)
                layout.addWidget(self.kelime1_input)

                ceviri_button = QPushButton("Çeviri yap.")
                ceviri_button.clicked.connect(self.mesaj)
                layout.addWidget(ceviri_button)

                label_kelime2 = QLabel()
                self.kelime2_input = QLineEdit()
                layout.addWidget(label_kelime2)
                layout.addWidget(self.kelime2_input)

                central_widget.setLayout(layout)
                self.setCentralWidget(central_widget)

        def mesaj(self):
                kelime1 = int(self.kelime1_input.text()) * 2
                self.kelime2_input.setText(str(kelime1))

def main():
        app= QApplication(sys.argv)
        window1 = loginEkrani()
        window = cevirmeEkrani()
        QMessageBox.information(window, "TR-ENG Sözlük", "Sözlük uygulamasına hoş geldiniz.")
        window.show()
        sys.exit(app.exec())

if __name__ == "__main__":
        main()