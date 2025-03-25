import fitz
from PIL import Image as pilIm

def generate_thumbnail(pdf_path, output_path, width, height):
    # Open the PDF file
    doc = fitz.open(pdf_path)

    # Get the first page of the PDF
    page = doc[0]

    # Create a thumbnail of the page
    pix = page.get_pixmap(matrix=fitz.Matrix(1, 1).prescale(width / page.rect.width, height / page.rect.height))
    pix.save(output_path)

    # Close the PDF file
    doc.close()

# n=300
# # Generate a thumbnail preview with a width of 200 pixels and a height of 300 pixels
# generate_thumbnail("input.pdf", "output.png", n*1.44, n)