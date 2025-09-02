import base64
from transformers import AutoProcessor, AutoModelForVision2Seq
import sys
import pypdfium2 as pdfium
import torch
from transformers import AutoProcessor, AutoModelForImageTextToText

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
        
        # Encode image to base64
        with open(file_name, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

        # Load the model
        model_id = "Qwen/Qwen2.5-VL-7B-Instruct" 
        processor = AutoProcessor.from_pretrained(model_id)
        model = AutoModelForImageTextToText.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda").eval()

        # Define the prompt
        PROMPT = """
                Attached is one page of a document that you must process. 
                Just return the plain text representation of this document as if you were reading it naturally. 
                Convert equations to LateX and tables to markdown.
                Return your output as markdown
            """

        # Define the messages
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "image": encoded_string,
                    },
                    {"type": "text", "text": PROMPT},
                ],
            }
        ]

        # Apply the chat template
        inputs = processor.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt"
        ).to(model.device)

        # Generate the output
        output_ids = model.generate(**inputs, max_new_tokens=1000)
        generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(inputs.input_ids, output_ids)]
        # Decode the output
        output_text = processor.batch_decode(generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True)
        # Print the output
        print(output_text)

# Main function, receives the path to the pdf file
if __name__ == "__main__":
    process_pdf(sys.argv[1])