import PyPDF2

output = PyPDF2.PdfFileWriter()


file1 = open("Online_Dating.pdf", 'rb')
reader1 = PyPDF2.PdfFileReader(file1)

for pages in range(reader1.numPages):
    output.addPage(reader1.getPage(pages))

output.encrypt('taimur')

output_file = open('encrypted_output.pdf', 'wb')
output.write(output_file)
output_file.close()
file1.close()