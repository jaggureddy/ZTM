import PyPDF2

pdfs = ['C:\\Users\\JR0544\\PycharmProjects\\ZeroToMastery\\PDFs\\2020ViaBenefitsCostSummary.pdf',
        'C:\\Users\\JR0544\\PycharmProjects\\ZeroToMastery\\PDFs\\advanced_syllabus_2012_test_analyst_ga_release_20121019.pdf',
        'C:\\Users\\JR0544\\PycharmProjects\\ZeroToMastery\\PDFs\\Amex_Statement.pdf']


def pdf_merger(pdfs):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write('merge.pdf')


pdf_merger(pdfs)

