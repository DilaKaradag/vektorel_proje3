import sys
from PyQt6.QtWidgets import *

class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dila'nın Uygulaması.")
        self.arayuz()

    def arayuz(self):
        ana_widget = QWidget()
        layout = QVBoxLayout()
       
        layout.addWidget(QLabel("Hangi uygulamayı kullanacaksın?"))

        uygulama1 = QPushButton("Inch Çevirici")
        uygulama1.clicked.connect(self.uygulama1Tiklanma)
        layout.addWidget(uygulama1)

        uygulama2 = QPushButton("Vücut Kitle İndeksi Hesaplama")
        uygulama2.clicked.connect(self.uygulama2Tiklanma)
        layout.addWidget(uygulama2)

        ana_widget.setLayout(layout)
        self.setCentralWidget(ana_widget)

    def uygulama1Tiklanma(self):
        
        self.uygulama1 = InchCevirici()
        self.uygulama1.show()
   
    def uygulama2Tiklanma(self):
        
        self.uygulama2 = vucutkitleuygulamasi()
        self.uygulama2.show()

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Ekranı")
        self.arayuz()

    def arayuz(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        label_username = QLabel("Kullanıcı Adı:")
        self.username_input = QLineEdit()
        layout.addWidget(label_username)
        layout.addWidget(self.username_input)

        label_password = QLabel("Şifre:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(label_password)
        layout.addWidget(self.password_input)

        login_button = QPushButton("Giriş Yap")
        login_button.clicked.connect(self.login)
        layout.addWidget(login_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        
        if username == "admin" and password == "admin":
            self.open_AnaEkran()
        else: QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre!")

    def open_AnaEkran(self):
        QMessageBox.information(self, "Başarılı", "Giriş başarılı!\nKULLANMAK İSTEDİĞİNİZ BİR PROGRAM SEÇİNİZ")
        self.close()  
        self.anaEkran = AnaPencere()
        self.anaEkran.show()

class InchCevirici(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inch çevirici")
        self.arayuz()

    def arayuz(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        label_cmdeger = QLabel("Cm değeri girin:")
        self.cmdeger_input = QLineEdit()
        layout.addWidget(label_cmdeger)
        layout.addWidget(self.cmdeger_input)

        cevir_button = QPushButton("Çevir")
        cevir_button.clicked.connect(self.mesaj)
        layout.addWidget(cevir_button)

        label_inch = QLabel("Inch değeri:")
        self.inch_input = QLineEdit()
        layout.addWidget(label_inch)
        layout.addWidget(self.inch_input)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def mesaj(self):
        cmdeger = int(self.cmdeger_input.text()) * 0.393700787
        self.inch_input.setText(str(cmdeger))
       
class vucutkitleuygulamasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vücut Kitle İndeks")
       
        layout = QVBoxLayout() 
        self.yiginLayout = QStackedLayout() 
        self.setLayout(layout)
       
        label_kg = QLabel("Kilonuzu giriniz(kg):")
        self.kg_input = QLineEdit()
        layout.addWidget(label_kg)
        layout.addWidget(self.kg_input)

        label_boy = QLabel("Boyunuzu giriniz(m):")
        self.boy_input = QLineEdit()
        layout.addWidget(label_boy)
        layout.addWidget(self.boy_input)

        button = QPushButton("Hesapla")
        button.clicked.connect(self.mesaj2)
        layout.addWidget(button)
        
        label_indeks = QLabel("İndeksiniz:")
        self.indeks_input = QLineEdit()
        layout.addWidget(label_indeks)
        layout.addWidget(self.indeks_input)

    def mesaj2(self):
        sonuc = int(self.kg_input.text()) / float(self.boy_input.text()) ** 2
        self.indeks_input.setText(str(sonuc))

        if sonuc < 18.5:
            print(sonuc, "İdeal kilonun altındasınız.")
        elif 18.5 < sonuc < 24.9:
            print(sonuc, "İdeal kilodasınız.")
        elif 25 < sonuc < 29.9:
            print(sonuc, "İdeal kilonun üstündesiniz.")
        elif 30 < sonuc < 39.9:
            print(sonuc, "İdeal kilonun çok üstündesiniz.(OBEZ)")
        elif sonuc >= 40:
            print(sonuc, "İdeal kilonun çok üstündesiniz.(MORBİD OBEZ)")

        
        
        
def main():
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()