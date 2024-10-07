from pdfminer.high_level import extract_text

# Extract text with layout preservation
text = extract_text(r'D:\IGS\PB Data Utils Scripts\ocr\ocr_sample_input.pdf', laparams=None)

print(text)
