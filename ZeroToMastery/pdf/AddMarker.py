import PyPDF2

template = 'C:\\Users\\JR0544\\PycharmProjects\\ZeroToMastery\\PDFs\\2020ViaBenefitsCostSummary.pdf'
marker = 'C:\\Users\\JR0544\\PycharmProjects\\ZeroToMastery\\PDFs\\original.pdf'

# template = PyPDF2.PdfFileReader(open('C:\\Users\\JR0544\\PycharmProjects\\ZeroToMastery\\PDFs\\2020ViaBenefitsCostSummary.pdf', 'rb'))
# marker = PyPDF2.PdfFileReader(open('C:\\Users\\JR0544\\PycharmProjects\\ZeroToMastery\\PDFs\\original.pdf', 'rb'))
"""
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(marker.getPage(0))
    output.addPage(page)

with open('watermarker.pdf', 'wb') as file:
    output.write(file)
"""


def pdf_watermarker(original, watermark):
    wtr_file = open(watermark, 'rb')

    original_file = open(original, 'rb')
    original_reader = PyPDF2.PdfFileReader(original_file)

    writer = PyPDF2.PdfFileWriter();

    for original_page in original_reader.pages:
        wtr_reader = PyPDF2.PdfFileReader(wtr_file)
        wtr_page = wtr_reader.getPage(0)
        wtr_page.mergePage(original_page)
        writer.addPage(wtr_page)

    with open('watermarker.pdf', 'wb') as file:
        writer.write(file)
    original_file.close()
    wtr_file.close()


pdf_watermarker(template, marker)
