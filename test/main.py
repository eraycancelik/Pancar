import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget

class AnaEkran(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ana Ekran")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()
        self.lineEdit = QLineEdit()
        layout.addWidget(self.lineEdit)

        button = QPushButton("Aç")
        button.clicked.connect(self.ac_buton_tiklandi)
        layout.addWidget(button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def ac_buton_tiklandi(self):
        girilen_metin = self.lineEdit.text()
        self.ekran = IkinciEkran(girilen_metin)
        self.ekran.exec()

class IkinciEkran(QDialog):
    def __init__(self, metin):
        super().__init__()
        self.setWindowTitle("İkinci Ekran")
        self.setGeometry(200, 200, 400, 200)

        layout = QVBoxLayout()
        self.label = QLabel("Ana Ekran'dan gelen metin: " + metin)
        layout.addWidget(self.label)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ana_ekran = AnaEkran()
    ana_ekran.show()
    sys.exit(app.exec())
