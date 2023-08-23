import os
import base64
from PIL import Image
from io import BytesIO

def process_image(image_data_b64):
    # Convert base64 image data to Image
    image_data = base64.b64decode(image_data_b64)
    image = Image.open(BytesIO(image_data))
    image_filename = f"temp_{os.urandom(4).hex()}.png"
    image.save(image_filename)

    # Process with Tesseract
    os.system(f"tesseract --psm 1 --oem 1 {image_filename} output")
    with open("output.txt", "r") as f:
        recognized_text = f.read().strip()

    # Cleanup temp files
    os.remove(image_filename)

    return recognized_text
