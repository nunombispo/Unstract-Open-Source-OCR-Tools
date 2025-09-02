# Unstract Open Source OCR Tools

A comprehensive collection of open-source OCR (Optical Character Recognition) tools and examples for document processing. This project provides implementations using various state-of-the-art OCR libraries and models to extract text from PDF documents and images.

## 🚀 Features

- **Multiple OCR Engines**: Support for EasyOCR, DocTR, Surya OCR, olmOCR, and Qwen2.5-VL
- **PDF Processing**: Convert PDF pages to images for OCR processing
- **GPU Acceleration**: Support for GPU-accelerated processing where available
- **Multiple Languages**: EasyOCR supports multiple languages
- **Advanced Models**: Integration with cutting-edge vision-language models
- **Ready-to-Use Examples**: Complete working examples for each OCR tool

## 📋 Supported OCR Tools

### 1. **EasyOCR**

- **Description**: A popular, easy-to-use OCR library with support for 80+ languages
- **Features**:
  - Multi-language support
  - GPU acceleration
  - Paragraph-level text extraction
  - High accuracy for printed text
- **Best For**: General document OCR, multi-language documents

### 2. **DocTR**

- **Description**: Document Text Recognition library by Mindee
- **Features**:
  - Document understanding capabilities
  - Structured output (words, lines, blocks)
  - Pre-trained models
  - JSON export functionality
- **Best For**: Document analysis, structured text extraction

### 3. **Surya OCR**

- **Description**: Advanced OCR system with detection and recognition capabilities
- **Features**:
  - Text detection and recognition
  - Foundation model integration
  - High accuracy for complex layouts
- **Best For**: Complex document layouts, high-accuracy requirements

### 4. **olmOCR**

- **Description**: Large vision-language model for document understanding
- **Features**:
  - 7B parameter model
  - Natural language understanding
  - Equation and table conversion
  - Markdown output
- **Best For**: Complex documents with equations, tables, and mixed content

### 5. **Qwen2.5-VL**

- **Description**: Alibaba's vision-language model for document processing
- **Features**:
  - 7B parameter model
  - Advanced document understanding
  - LaTeX equation conversion
  - Markdown table formatting
- **Best For**: Advanced document analysis, mathematical content

## 🛠️ Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/nunombispo/Unstract-Open-Source-OCR-Tools
   cd Unstract-Open-Source-OCR-Tools
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Additional setup for GPU support** (optional):
   ```bash
   # Install PyTorch with CUDA support
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```

## 📖 Usage

### Basic Usage

Each OCR tool has its own example script. To use any of them:

```bash
python tool_name_example.py path/to/your/document.pdf
```

### Examples

#### EasyOCR

```bash
python easyocr_example.py docs/bank-statement-complex-layout.pdf
```

#### DocTR

```bash
python doctr_example.py docs/handwritten-document-1.pdf
```

#### Surya OCR

```bash
python surya_example.py docs/Insurance-plan-details-complex-tables.pdf
```

#### olmOCR

```bash
python olmocr_example.py docs/universal_loan_application_filled_checkboxes.pdf
```

#### Qwen2.5-VL

```bash
python qwen_example.py docs/poorly-aligned-receipt.pdf
```

## 📁 Project Structure

```
Unstract-Open-Source-OCR-Tools/
├── docs/                          # Sample PDF documents for testing
│   ├── bank-statement-complex-layout.pdf
│   ├── handwritten-Airway_bill_photographed.pdf
│   ├── handwritten-document-1.pdf
│   ├── Insurance-plan-details-complex-tables.pdf
│   ├── poorly-aligned-receipt.pdf
│   └── universal_loan_application_filled_checkboxes.pdf
├── easyocr_example.py             # EasyOCR implementation
├── doctr_example.py               # DocTR implementation
├── surya_example.py               # Surya OCR implementation
├── olmocr_example.py              # olmOCR implementation
├── qwen_example.py                # Qwen2.5-VL implementation
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## 🔧 Requirements

- **Python**: 3.8+
- **PyTorch**: For GPU acceleration (optional)
- **CUDA**: For GPU support (optional)
- **Memory**: At least 8GB RAM (16GB+ recommended for large models)

### Key Dependencies

- `easyocr`: Multi-language OCR library
- `python-doctr`: Document text recognition
- `surya-ocr`: Advanced OCR system
- `transformers`: Hugging Face transformers for vision-language models
- `pypdfium2`: PDF to image conversion
- `torch`: PyTorch for deep learning models

## 🎯 Use Cases

### Document Types Supported

- **Bank Statements**: Complex layouts with tables and numbers
- **Handwritten Documents**: Notes, forms, and signatures
- **Insurance Documents**: Complex tables and structured data
- **Receipts**: Poorly aligned and low-quality scans
- **Loan Applications**: Forms with checkboxes and structured fields
- **Airway Bills**: Shipping and logistics documents

### OCR Tool Selection Guide

| Document Type            | Recommended Tool  | Reason                      |
| ------------------------ | ----------------- | --------------------------- |
| Multi-language documents | EasyOCR           | Best language support       |
| Structured documents     | DocTR             | Better layout understanding |
| Complex layouts          | Surya OCR         | Advanced detection          |
| Mathematical content     | olmOCR/Qwen2.5-VL | LaTeX equation support      |
| Mixed content            | Qwen2.5-VL        | Advanced understanding      |

## 🚀 Performance Tips

1. **GPU Acceleration**: Enable GPU support for faster processing
2. **Batch Processing**: Process multiple documents in sequence
3. **Memory Management**: Close PDF files after processing
4. **Model Selection**: Choose the right tool for your document type
5. **Image Quality**: Ensure good quality scans for better results

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 🙏 Acknowledgments

- [EasyOCR](https://github.com/JaidedAI/EasyOCR) - Multi-language OCR library
- [DocTR](https://github.com/mindee/doctr) - Document Text Recognition
- [Surya OCR](https://github.com/VikParuchuri/surya) - Advanced OCR system
- [olmOCR](https://huggingface.co/allenai/olmOCR-7B-0725) - Vision-language model
- [Qwen2.5-VL](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct) - Alibaba's vision-language model
