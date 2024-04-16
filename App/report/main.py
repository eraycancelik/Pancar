# Python libraries
from fpdf import FPDF
import matplotlib.pyplot as plt
# Local libraries



def create_analytics_report(filename="te.pdf"):
    WIDTH = 210
    HEIGHT = 297
    
    pdf = FPDF() # A4 (210 by 297 mm)
    pdf.add_page()
    pdf.image("./pancar_pdf.png", 0, 0, WIDTH)
    
    pdf.set_font('Arial', '', 24)

    list_a = [i for i in range(0, 90)]
    list_b = [i * 2 for i in list_a]
    
    # Çizimi oluştur
    plt.plot(list_a, list_b)
    plt.savefig("plot.png")  # Çizimi bir dosyaya kaydet
    
    # PDF dosyasına çizimi ekle
    pdf.image("plot.png", x=10, y=50, w=100)
    
    # PDF dosyasını kaydet
    pdf.output(filename, 'F')


if __name__ == '__main__':
  create_analytics_report()
