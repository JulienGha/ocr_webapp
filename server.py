from flask import Flask, request, jsonify
from flask_cors import CORS
from rq import Queue
from worker import conn
from tasks import simple_task, process_image_from_path, run_tesseract
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)
q = Queue(connection=conn)
ALLOWED_EXTENSIONS = {'png', 'tiff', 'tif'}    # defining the possible file format


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/image', methods=['POST'])
def post_image():

    job = None
    if 'image' not in request.files:
        return jsonify({"error": "No image part in the request"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    job = q.enqueue(simple_task)

    unique_id = datetime.now().strftime("%Y%m%d%H%M%S")

    os.makedirs("./temp_files", exist_ok=True)

    if file and allowed_file(file.filename):
        # Enqueue the image processing task
        temp_filename = unique_id + "." + file.filename.rsplit('.', 1)[1].lower()
        file.save(f"./temp_files/{temp_filename}")
        job = q.enqueue(run_tesseract, temp_filename, job_id=unique_id)

    if job:
        return jsonify({"task_id": job.get_id()}), 202
    else:
        return jsonify({"error": "Failed to enqueue job"}), 500


@app.route('/image', methods=['GET'])
def get_image():
    task_id = request.args.get('task_id')
    if not task_id:
        return jsonify({"error": "task_id is required"}), 400

    job = q.fetch_job(task_id)
    if not job:
        return jsonify({"error": "No such task"}), 404

    if job.is_finished:
        return jsonify({"result": job.result}), 200
    else:
        return jsonify({"result": None}), 202


@app.route('/test', methods=['GET'])
def get_test():
    return "good"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
