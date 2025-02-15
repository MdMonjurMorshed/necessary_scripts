from io import BytesIO

import requests
from PyPDF2 import PdfMerger

pdf_merger = PdfMerger()


urls = [
    "https://evidentbd.sgp1.cdn.digitaloceanspaces.com/mye/42087E963F.pdf",
    "https://evidentbd.sgp1.cdn.digitaloceanspaces.com/mye/9FA1C2CEF5.pdf",
    "https://evidentbd.sgp1.cdn.digitaloceanspaces.com/mye/2797512EAC.pdf",
    "https://evidentbd.sgp1.cdn.digitaloceanspaces.com/mye/6B0032B33D.pdf"
]

for url in urls:
    file_pdf = requests.get(url)
    file_path = BytesIO(file_pdf.content)
    pdf_merger.append(file_path)
print(pdf_merger)

output_file = "merged_output.pdf"

pdf_merger.write(output_file)
pdf_merger.close()

print("pdf file merged")


