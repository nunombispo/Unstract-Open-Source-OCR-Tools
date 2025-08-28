from doctr.io import DocumentFile
from doctr.models import ocr_predictor
import sys

# Process the pdf file
def process_pdf(pdf_path):
    model = ocr_predictor(pretrained=True)
    # PDF
    doc = DocumentFile.from_pdf(pdf_path)
    # Analyze
    result = model(doc)
    # Export the result
    json_output = result.export()
    for page in json_output['pages']:
        for block in page['blocks']:
            for line in block['lines']:
                for word in line['words']:
                    print(word['value'])

# Main function, receives the path to the pdf file
if __name__ == "__main__":
    process_pdf(sys.argv[1])