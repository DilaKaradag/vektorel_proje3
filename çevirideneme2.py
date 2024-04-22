import googletrans
import sys
import language
import login
from PyQt6.QtWidgets import *


class cevirmeEkrani(QMainWindow):
        
        
        def __init__(self):
                super().__init__()

                self.setWindowTitle("TR-ENG SÖZLÜK")
                self.arayuz()

        def arayuz(self):
                central_widget = QWidget()
                layout = QVBoxLayout()

                label_kelime1 = QLabel("Kelimeyi giriniz(TR): ")
                self.kelime1_input = QLineEdit()
                layout.addWidget(label_kelime1)
                layout.addWidget(self.kelime1_input)

                ceviri_button = QPushButton("Çeviri yap")
                ceviri_button.clicked.connect(self.mesaj)
                layout.addWidget(ceviri_button)

                label_kelime2 = QLabel("Sonuç(ENG): ")
                self.kelime2_input = QLineEdit()
                layout.addWidget(label_kelime2)
                layout.addWidget(self.kelime2_input)

                central_widget.setLayout(layout)
                self.setCentralWidget(central_widget)

                

                

        def mesaj(self):
                kelime1 = (self.kelime1_input.text()) == "Turkish"
                self.kelime2_input.setText(str(kelime1)) == "English"

def main():
        app= QApplication(sys.argv)
        window = cevirmeEkrani()
        QMessageBox.information(window, "TR-ENG Sözlük", "Sözlük uygulamasına hoş geldiniz.")
        window.show()
        sys.exit(app.exec())

if __name__ == "__main__":
        main()