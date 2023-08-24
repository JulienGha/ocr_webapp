import os
from werkzeug.datastructures import FileStorage


def process_image(file: FileStorage):
    # Ensure the passed object is a file
    if not isinstance(file, FileStorage):
        raise ValueError("Expected FileStorage object as input.")

    # Create a temporary filename
    image_filename = f"temp_{os.urandom(4).hex()}.png"

    # Save the uploaded image
    file.save(image_filename)

    # Process with tesseract
    os.system(f"tesseract --psm 1 --oem 1 {image_filename} output")

    # Read the output
    with open("output.txt", "r") as f:
        recognized_text = f.read().strip()

    # Cleanup temp files
    os.remove(image_filename)

    return recognized_text
