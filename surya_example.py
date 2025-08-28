from surya.foundation import FoundationPredictor
from surya.recognition import RecognitionPredictor
from surya.detection import DetectionPredictor
import pypdfium2 as pdfium
import sys


# Process the pdf file
def process_pdf(pdf_path):
    # Load a document
    pdf = pdfium.PdfDocument(pdf_path)

    # Loop over pages and render
    for i in range(len(pdf)):
        page = pdf[i]
        image = page.render(scale=1).to_pil()
        
        print(f"Processing page {i+1}...")
        foundation_predictor = FoundationPredictor()
        recognition_predictor = RecognitionPredictor(foundation_predictor)
        detection_predictor = DetectionPredictor()

        predictions = recognition_predictor([image], det_predictor=detection_predictor)
        print(f"Page {i+1} OCR Results:")
        for prediction in predictions:
            for text_lines in prediction.text_lines:
                print(text_lines.text)

    # Close the PDF
    pdf.close()

# Main function, receives the path to the pdf file
if __name__ == "__main__":
    process_pdf(sys.argv[1])