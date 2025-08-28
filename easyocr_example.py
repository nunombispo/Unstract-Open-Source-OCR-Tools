import easyocr
import pypdfium2 as pdfium
import sys

# Create a reader object (multiple languages can be specified, and here it will run on CPU)
reader = easyocr.Reader(['en'], gpu=False)

# Process the pdf file
def process_pdf(pdf_path):
    # Load a document
    pdf = pdfium.PdfDocument(pdf_path)

    # Loop over pages and render
    for i in range(len(pdf)):
        page = pdf[i]
        image = page.render(scale=1).to_pil()

        # Save image
        file_name = f"docs/output/page_{i+1}.png"
        image.save(file_name)
        
        # Read the text from the image
        print(f"Processing page {i+1}...")
        result = reader.readtext(file_name, detail=0, paragraph=True)
        
        # Print the result
        print(f"Page {i+1} OCR Results:")
        print(result)

    # Close the PDF
    pdf.close()

# Main function, receives the path to the pdf file
if __name__ == "__main__":
    process_pdf(sys.argv[1])