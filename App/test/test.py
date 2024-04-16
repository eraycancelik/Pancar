import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from fpdf import FPDF

class PDFGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Analiz Raporu Oluşturucu")
        self.setGeometry(100, 100, 400, 200)

        self.button = QPushButton("Rapor Oluştur", self)
        self.button.setGeometry(150, 80, 100, 40)
        self.button.clicked.connect(self.generate_pdf)

    def generate_pdf(self):
        # Dosya kaydetme iletişim kutusunu aç
        options = QFileDialog.options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Raporu Kaydet", "", "PDF Dosyaları (*.pdf)", options=options)
        
        if file_path:
            # Rapor oluşturma işlemleri
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Bu bir PDF analiz raporudur.", ln=True)
            pdf.output(file_path)
            print("Rapor başarıyla oluşturuldu ve kaydedildi:", file_path)

def main():
    app = QApplication(sys.argv)
    window = PDFGenerator()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
