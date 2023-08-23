from flask import Flask, request, jsonify
from rq import Queue
from worker import conn
from tasks import process_image

app = Flask(__name__)
q = Queue(connection=conn)


@app.route('/image', methods=['POST'])
def post_image():
    image_data = request.json.get('image_data')
    
    # Enqueue the image processing task
    job = q.enqueue(process_image, image_data)
    
    return jsonify({"task_id": job.get_id()}), 202


@app.route('/image', methods=['GET'])
def get_image():
    task_id = request.json.get('task_id')
    job = q.fetch_job(task_id)
    
    if job.is_finished:
        return jsonify({"task_id": job.result}), 200
    else:
        return jsonify({"task_id": None}), 202


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
