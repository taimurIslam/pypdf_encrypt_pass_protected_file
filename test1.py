from PyPDF2 import PdfFileReader, PdfFileWriter

output = PdfFileWriter()

file1 = open("Online_Dating.pdf", 'rb')
file2 = open("Online_Dating_1.pdf", 'rb')

reader1 = PdfFileReader(file1)
reader2 = PdfFileReader(file2)

for page_num in range(reader1.numPages):
    file1_pages = reader1.getPage(page_num)
    output.addPage(file1_pages)

for page_num in range(reader2.numPages):
    file2_pages = reader2.getPage(page_num)
    output.addPage(file2_pages)

output_file = open('output.pdf', 'wb')
output.write(output_file)
output_file.close()
file1.close()
file2.close()