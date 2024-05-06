from fpdf import FPDF

# Alt listeleri bulunan ana liste
data = [
    ["A1", "B1"],
    ["A2", "B2"],
    ["A3", "B3"],
    ["A4", "B4"],
    ["A5", "B5"]
]

# PDF nesnesi oluşturma
pdf = FPDF()
pdf.add_page()

# Font ayarı
pdf.set_font("Arial", size=12)

# Tablo oluşturma
pdf.set_fill_color(200, 220, 255)
pdf.set_draw_color(0, 0, 0)
cell_width = 40
cell_height = 10

# Başlık satırı
pdf.set_font("Arial", style="B", size=12)
pdf.cell(cell_width, cell_height, "Column 1", border=1)
pdf.cell(cell_width, cell_height, "Column 2", border=1)
pdf.ln()

# Veri satırları
pdf.set_font("Arial", size=12)
for row in data:
    for item in row:
        pdf.cell(cell_width, cell_height, item, border=1)
    pdf.ln()

# PDF dosyasını kaydetme
pdf.output("table.pdf")

