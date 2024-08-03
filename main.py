import fitz # PyMuPDF
import subprocess


pdf_path = input('enter pdf path: ')

def speechify(text):
    command = f'cat text.txt | piper/piper --module norman/en_US-norman-medium.onnx --output_file {pdf_path}.wav'

    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True)

    # print(result)



def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    # return text
    
    with open('text.txt', 'w') as file:
        file.write(text)


text = extract_text_from_pdf(pdf_path)
# print(text)
speechify(text)



