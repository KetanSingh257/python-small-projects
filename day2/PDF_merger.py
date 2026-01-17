from PyPDF2 import PdfMerger

merger = PdfMerger()


n = int(input("Enter the number of PDF files to merge: "))

for i in range(n):
    pdf = input(f"Enter the path to PDF file {i+1}: ")  
    merger.append(pdf)
    

    
merger.write("merged-pdf.pdf")
merger.close()
print("PDF files merged successfully into 'merged-pdf.pdf'")