import os


def run_tesseract(input_file):
    cmd = f"docker run --rm -v ./temp_files/:/mnt tesseract:0.1 /mnt/{input_file} stdout"
    os.system(cmd)
    cmd = f"docker run --rm -v ./temp_files/:/mnt tesseract:0.1 /mnt/{input_file} output"
    os.system(cmd)
    # Cleanup temp files
    os.remove(f"./temp_files/{input_file}")
    # Read the output
    with open("output.txt", "r") as f:
        recognized_text = f.read().strip()
    return recognized_text


def simple_task():
    print("Task was picked up by worker.")


def process_image_from_path(file_name: str):

    print("Processing image started...")

    cmd = f"tesseract --psm 1 --oem 1 {file_name} output"
    os.system(cmd)

    # Read the output
    with open("output.txt", "r") as f:
        recognized_text = f.read().strip()

    # Cleanup temp files
    os.remove(f"./temp_files/{file_name}")

    print("Processing image completed.")
    return recognized_text
