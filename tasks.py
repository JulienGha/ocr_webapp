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

