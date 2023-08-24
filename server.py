from flask import Flask, request, jsonify
from flask_cors import CORS
from rq import Queue
from worker import conn
from tasks import process_image

app = Flask(__name__)
CORS(app)
q = Queue(connection=conn)
ALLOWED_EXTENSIONS = {'png', 'tiff'}    # defining the possible file format


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/image', methods=['POST'])
def post_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image part in the request"}), 400
    file = request.files['image']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        # Enqueue the image processing task
        job = q.enqueue(process_image, file)
    
    return jsonify({"task_id": job.get_id()}), 202


@app.route('/image', methods=['GET'])
def get_image():
    task_id = request.json.get('task_id')
    job = q.fetch_job(task_id)
    
    if job.is_finished:
        return jsonify({"task_id": job.result}), 200
    else:
        return jsonify({"task_id": None}), 202


@app.route('/test', methods=['GET'])
def get_test():
    return "good"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
