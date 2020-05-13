import PyPDF2

with open('C:\\Users\\JR0544\\PycharmProjects\\ZeroToMastery\\PDFs\\2020ViaBenefitsCostSummary.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    # print(reader.getNumPages())
    # print(reader.getPage(0))
    print(page.rotateClockwise(90))
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as file1:
        writer.write(file1)
