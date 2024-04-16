# Python libraries
from fpdf import FPDF
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from io import BytesIO
# Local libraries

WIDTH = 210
HEIGHT = 297

TEST_DATE = "10/20/20"


def create_analytics_report(day=TEST_DATE, filename="dosya.pdf"):
    pdf = FPDF() # A4 (210 by 297 mm)
    ''' First Page '''
    pdf.add_page()
    pdf.image("./pancar_pdf.png", 0, 0, WIDTH)
    list_a = [i for i in range(0, 90)]
    list_b = [i * 2 for i in list_a]
    
    # Çizimi oluştur
    fig, ax = plt.subplots()
    ax.plot(list_a, list_b)
    
    # Çizimi bir bayt dizesi olarak sakla
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    
    # Bayt dizesini PDF dosyasına ekle
    pdf.image(buffer.getvalue(), x=10, y=50, w=100)

    # PDF dosyasını kaydet
    pdf.output(filename, 'F')


if __name__ == '__main__':
  create_analytics_report()
