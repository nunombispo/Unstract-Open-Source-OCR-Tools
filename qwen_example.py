import sys
from ollama import chat
from ollama import ChatResponse
import pypdfium2 as pdfium

# Process the pdf file
def process_pdf(pdf_path):
    # Load a document
    pdf = pdfium.PdfDocument(pdf_path)

    # Loop over pages and render
    image_list = []
    for i in range(len(pdf)):
        page = pdf[i]
        image = page.render(scale=1).to_pil()

        # Save image
        file_name = f"docs/output/page_{i+1}.png"
        image.save(file_name)
        image_list.append(file_name)

    print("Processing PDF file: ", pdf_path)
    response: ChatResponse = chat(model='qwen2.5vl:7B', messages=[
    {
        'role': 'user',
        'content': """You are a helpful assistant that can extract text from a pdf file passed in as individual images. 
                        Please extract the text from the images and return it a way that the layout is preserved.
                        """,
        'images': image_list
    },
    ])
    # Print the response
    print(response.message.content)

# Main function, receives the path to the pdf file
if __name__ == "__main__":
    process_pdf(sys.argv[1])