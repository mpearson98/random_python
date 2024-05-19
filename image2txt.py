import os
from PIL import Image
import pytesseract

# Define the directory to scan
directory = '/path/to/directory'

# Walk through the directory
for root, dirs, files in os.walk(directory):
    for file in files:
        # Check if the file is an image
        if file.endswith(('.png', '.jpg', '.jpeg')):
            # Construct the full file path
            file_path = os.path.join(root, file)
            
            # Open the image
            image = Image.open(file_path)

            # Perform OCR on the image
            text = pytesseract.image_to_string(image)

            # Print the extracted text
            print(f'OCR result for {file_path}:')
            print(text)
            print('---')