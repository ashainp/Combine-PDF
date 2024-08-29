# First, make sure you have Python installed on your system.
# You also need to install the PyPDF2 package.
# To install PyPDF2, open your command prompt and run:
# pip install PyPDF2

import PyPDF2

# Function to combine PDFs, inserting one PDF before the last page of another
def insert_pdf_before_last(base_pdf_path, insert_pdf_path, output_pdf_path):
    # Load PDF 1 (base PDF)
    with open(base_pdf_path, 'rb') as base_pdf_file:
        base_pdf = PyPDF2.PdfReader(base_pdf_file)
        
        # Load PDF 2 (the PDF to be inserted)
        with open(insert_pdf_path, 'rb') as insert_pdf_file:
            insert_pdf = PyPDF2.PdfReader(insert_pdf_file)
            
            # Create a PDF writer object for the output
            pdf_writer = PyPDF2.PdfWriter()
            
            # Add all pages from the base PDF except the last one
            for page_num in range(len(base_pdf.pages) - 1):
                pdf_writer.add_page(base_pdf.pages[page_num])
            
            # Insert all pages from the second PDF
            for page_num in range(len(insert_pdf.pages)):
                pdf_writer.add_page(insert_pdf.pages[page_num])
            
            # Add the last page of the base PDF
            pdf_writer.add_page(base_pdf.pages[-1])
            
            # Write the output to a new PDF file
            with open(output_pdf_path, 'wb') as output_file:
                pdf_writer.write(output_file)

# --- User Instructions: Specify the file paths below ---

# The base PDF path: Replace with the full path to your base PDF file
base_pdf_path = r'C:\Users\enoks\Desktop\AI\Combine PDF\ARR.pdf'

# The PDF to insert: Replace with the full path to your insert PDF file
insert_pdf_path = r'C:\Users\enoks\Desktop\AI\Combine PDF\White.pdf'

# The output PDF path: Replace with the full path where you want the combined PDF to be saved
output_pdf_path = r'C:\Users\enoks\Desktop\AI\Combine PDF\combined.pdf'

# Call the function to combine the PDFs
insert_pdf_before_last(base_pdf_path, insert_pdf_path, output_pdf_path)

print("PDFs have been combined successfully!")

# --- Additional Options ---

# If you want to combine more than two PDFs or insert another document:
# 1. Load additional PDFs using PyPDF2.PdfReader() and specify the paths.
# 2. Use pdf_writer.add_page() to append these additional pages before or after the current insert.
# 3. Adjust the code above to insert the new PDFs at the desired location.
# Example: Adding an additional PDF before inserting the last page of the base PDF.
# with open(additional_pdf_path, 'rb') as additional_pdf_file:
#     additional_pdf = PyPDF2.PdfReader(additional_pdf_file)
#     for page_num in range(len(additional_pdf.pages)):
#         pdf_writer.add_page(additional_pdf.pages[page_num])

# You can customize this script further to meet your needs!
