import pypdf
''' PyPDF is a Python library 
used to read, modify, merge, split, encrypt, decrypt, and extract data from PDF files. '''

"""PDF READER"""

reader = PdfReader ("sample.pdf")
print(lem(reader.pages))  #Number of pages

page = reader.pages[0]
print(page.extract_text())

"""EXTRACTING ALL THE TEXT FROM A PDF"""

writer = PdfWriter()
all_text = ''
for page in reader.pages:
    page_text = age.extract_text()
    if page_text:
        all_text += page_text + '\n'

print('All pdf text are: ')
print(all_text)


"""SPLITTING A PDF"""

for page_num , page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    output_name = f'page_{page_num+1}.pdf'
    writer.write(output_name)

"""ROTATE PAGES"""

reader = PdfReader("input.pdf")
writer = PdfWriter()

page = reader.pages[0]
page.rotate(90)

writer.add_page(page)

with open("rotated.pdf", "wb") as f:
    writer.write(f)


"""ENCRYPT A PDF"""

writer = PdfWriter()
for page in reader.pages:
    writer.add_page(page)

writer.encrypt('mypassword')
writer.write('protected_out.pdf')


"""DECRYPT A PDF"""

reader = PdfReader("encrypted.pdf")

reader.decrypt("mypassword")

print(reader.pages[0].extract_text())

"""MERGING PDF"""

writer = PdfWriter()
for file_name in ['sample.pdf' , 'second.pdf']:
    input_pdf = PdfReader(file_name)
    for page in input_pdf.pages:
        writer.add_page(page)

writer.write('merged pdf')


"""TO ADD A METADATA TO A PDF"""

writer = PdfWriter()
for page in reader.pages:
    writer.add_page(page)
    writer.add_metadata({'/Title' : 'My Custom PDF' , '/Author' : 'Youtube Demo'})
    writer.write('metadata_sample.pdf')

"""COPY ONLT ODD PAGES TO A NEW PDF (INTERMEDIATE)"""

writer = PdfWriter()
for page_num , page in enumerate(reader.pages):
    if page_num % 2 == 0:
        writer.add_page(page)

writer.write('odd_pages.pdf')


"""EXTRACT PDF METADATA (INTERMEDIATE)"""

meta = reader.metadata
for key , value in meta.items():
    print(f'{key}:{value}')


"""LINEARING A PDF FOR FAST WEB VIEW(ADVANCED)"""


writer = PdfWriter()
for page in reader.pages:
    writer.add_page(page)

writer.write('linearized_sample.pdf')


"""CATCH MISSING FILE ERRORS(ERROR HANDLING)"""

try:
    missing_reader = PdfReader('missing.pdf')
except:
    print('File mssing.pdf not found! Check the file name.')


"""WARN WHEN EXTRACTING TEXT RETURNS NONE(ERROR HANDLING)"""

page = reader.pages[0]
text = page.extract_text()
if text is None:
    print('No text extracted. This page may be scanned or image-only')
else:
    print('Text: ' , text)


"""ALWAYS CLOSE WRITERS FOR BEST PRACTICE"""

writer = PdfWriter()
for page in reader.pages:
    writer.add_page(page)
with open ('best_practice.pdf' , 'wb')as out_file:
    writer.write(out_file)


"""CHECK FOR ENCRYPTION BEFORE EXTRACTING TEXT(BEST PRACTICE)"""

if reader.is_encrypted:
    print('PDF is encrypted! Cannot extract text without the password.')
else:
    text = reader.pages[0].extract_text()
    print('Extracted text: ' , text)


"""GET TOTAL SIZE OF ALL PDF OUTPUTS (COMMON PATTERN)"""

import os
total_size = 0
for name in ['merged.pdf' , 'best_practice.pdf' , 'odd_pages.pdf']:
    if os.path.exists(name):
        total_size += os.path.getsize(name)

print('Total size in bytes: ' , total_size)


"""TINY MINI-PROJECT: COMBINING ONLY THE FIRST PAGES OF SEVERAL PDFS"""


import glob
writer = PdfWriter()
for pdf_file in glob.glob('*.pdf'):
    try:
        pdf = PdfReader(pdf_file)
        first_page = pdf.pages[0]
        writer.add_pages(first_page)
        print(f'Added first page from {pdf_file}')
    except Exception as e:
        print(f'Cannot add {pdf_file}: ' ,e)
writer.write('first_pages_collection.pdf')






