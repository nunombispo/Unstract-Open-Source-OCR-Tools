# Load model directly
from transformers import AutoProcessor, AutoModelForVision2Seq

processor = AutoProcessor.from_pretrained("allenai/olmOCR-7B-0725")
model = AutoModelForVision2Seq.from_pretrained("allenai/olmOCR-7B-0725")
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"},
            {"type": "text", "text": "What animal is on the candy?"}
        ]
    },
]
inputs = processor.apply_chat_template(
	messages,
	add_generation_prompt=True,
	tokenize=True,
	return_dict=True,
	return_tensors="pt",
    use_fast=True,
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=40)
print("Output")
print(processor.decode(outputs[0][inputs["input_ids"].shape[-1]:]))