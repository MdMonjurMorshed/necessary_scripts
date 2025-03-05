import fitz  # PyMuPDF
import pdfplumber

pdf_path = "example.pdf"
output_pdf = "modified_example_8.pdf"

# Extract text using pdfplumber
with pdfplumber.open(pdf_path) as pdf:
    first_page = pdf.pages[0]

    text = first_page.extract_text()
    print("printed text:",text)  # Print extracted text

# Open PDF with PyMuPDF
doc = fitz.open(pdf_path)
page = doc[0]
print(page)
# print("font details:",page.get_text('dict'))
# for k,v in page.get_text('dict').items():
    # print('===========',k,page.get_text('dict').get("blocks"))
font_familly = ''
font_size = 0    
for item in page.get_text('dict').get("blocks"):
    # print("========= item===",item.get('lines'))
    if item.get('lines'):
        # print(item.get('lines')[0].get('spans')[0].get('alpha'))
        if item.get('lines')[0].get('spans')[0].get('text').startswith('Course completed by'):
            print(item.get('lines')[0].get('spans'))
            print( item.get('lines')[0].get('spans')[0].get('text'))
            print( item.get('lines')[0].get('spans')[0].get('size'))
            font_familly = item.get('lines')[0].get('spans')[0].get('font')
            font_size = item.get('lines')[0].get('spans')[0].get('size')


# Replace text (manual or automated)
text_to_replace = "Md Monjur Morshed"  # Old name in certificate
new_text = "Jane Smith"

text_instances = page.search_for(text_to_replace)

for rect in text_instances:
    print("Found at:", rect)

    # Draw a white rectangle to erase text
    page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1))

    # Insert new text at the same position
    # page.insert_text((rect.x0, rect.y-1), new_text, fontsize=18, color=(0, 0, 0))
another_text = page.search_for("Course completed by")
for rect in another_text:
    new_rect_x = rect.x1+5
    new_rect_y = rect.y1-2
    print("font family",font_familly)
    page.insert_text((new_rect_x,new_rect_y),"Jhon Sina",fontsize=font_size,fontname=font_familly)    

# for text_instance in page.search_for(text_to_replace):
#     rect = text_instance  # Get bounding box of text
#     print('rect:',rect)
#     page.insert_text((rect.x0, rect.y0), new_text, fontsize=12, color=(0, 0, 0))  # Replace text

# Save modified PDF
# doc.save(output_pdf)
# doc.close()
# print(f"Modified PDF saved as {output_pdf}")
