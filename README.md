# Combine-PDF
A Python script to combine multiple PDFs, allowing the insertion of one PDF before the last page of another. Flexible for adding additional documents. Perfect for document management tasks.

# PDF Combiner

## Description
A Python script to combine multiple PDFs, allowing the insertion of one PDF before the last page of another. This tool is ideal for managing and organizing documents, providing flexibility for adding additional PDFs.

## Requirements
- Python 3.x
- PyPDF2

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ashainp/combine-PDF.git

2. Navigate to the directory
   cd combine-PDF

3. Install the required package
   pip install PyPDF2

##Usage
1. Update the file paths in the combine_pdfs.py script:

- base_pdf_path: The path to your base PDF file.
- insert_pdf_path: The path to the PDF file you want to insert.
- output_pdf_path: The path where the combined PDF will be saved.

2. Run script
   python combine.py

##Additional features
The script can be easily modified to add more PDFs in any sequence.

##Other functions 

1. Merge Multiple PDFs
This function merges multiple PDFs into a single document, combining all pages from several documents in the specified order.

def merge_pdfs(pdf_list, output_pdf_path):
    pdf_writer = PyPDF2.PdfWriter()
    for pdf in pdf_list:
        with open(pdf, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
    with open(output_pdf_path, 'wb') as output_file:
        pdf_writer.write(output_file)

2. Extract Text from PDFs
This function extracts and saves the text content of a PDF to a .txt file.

def extract_text(pdf_path, output_txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        with open(output_txt_path, 'w') as txt_file:
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                txt_file.write(page.extract_text())
                txt_file.write('\n')

3. Split a PDF into Separate Pages
This function splits a multi-page PDF into individual single-page PDFs.

def split_pdf(pdf_path, output_folder):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_num])
            output_path = f'{output_folder}/page_{page_num + 1}.pdf'
            with open(output_path, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

4. Add Watermarks to PDFs
This function adds a watermark to each page of a PDF using another PDF page as the watermark.

def add_watermark(input_pdf, output_pdf, watermark_pdf):
    with open(input_pdf, 'rb') as pdf_file, open(watermark_pdf, 'rb') as watermark_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        watermark_reader = PyPDF2.PdfReader(watermark_file)
        watermark_page = watermark_reader.pages[0]
        pdf_writer = PyPDF2.PdfWriter()
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page.merge_page(watermark_page)
            pdf_writer.add_page(page)
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

5. Encrypt PDFs with a Password
This function encrypts a PDF with a password to secure its contents.

def encrypt_pdf(input_pdf, output_pdf, password):
    pdf_writer = PyPDF2.PdfWriter()
    with open(input_pdf, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
        pdf_writer.encrypt(password)
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)


