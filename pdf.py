# pdf.py
# File: pdf.py

# from pypdf import PdfWriter # Alternate import for modern version
from PyPDF2 import PdfWriter

# 1. Create a PdfWriter object
pdfs = PdfWriter()

# 2. Get the number of PDFs to merge
n = int(input("How many pdfs do you want to merge?(*5)"))

# 3. Loop to get file names and append pages
for i in range(0, n):
    name = input(f"Enter the name of pdf {i+1}: ")
    # Append the pages from the current PDF to the PdfWriter object
    pdfs.append(name)

# 4. Final Merging and Output
for pdf in pdfs:
    print(f"pdf range: {pdf}")

# 5. Write the merged PDF to a new file
pdfs.write("merged-pdf.pdf")

