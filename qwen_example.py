import sys
from ollama import chat
from ollama import ChatResponse
import pypdfium2 as pdfium
import time
import ollama

# Pull the model
ollama.pull('qwen2.5vl:7b')

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
    start_time = time.time()
    response: ChatResponse = chat(model='qwen2.5vl:7b', messages=[
        {
            'role': 'user',
            'content': """
                            Attached is one page of a document that you must process. 
                            Just return the plain text representation of this document as if you were reading it naturally. 
                            Convert equations to LateX and tables to markdown.
                            Return your output as markdown
                        """,
            'images': image_list
        },
    ])
    # Print the response
    print(response.message.content)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

# Main function, receives the path to the pdf file
if __name__ == "__main__":
    process_pdf(sys.argv[1])