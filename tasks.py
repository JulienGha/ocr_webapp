import os


def run_tesseract(input_file):
    input_path = f"/data/temp_files/{input_file}"
    output_path = f"/data/temp_files/output_{input_file}.txt"
    cmd = f"tesseract {input_path} {output_path.rsplit('.', 1)[0]}"
    os.system(cmd)

    os.remove(input_path)

    with open(output_path, "r") as f:
        recognized_text = f.read().strip()

    os.remove(output_path)

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
