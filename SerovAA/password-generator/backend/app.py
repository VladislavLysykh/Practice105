from flask import Flask, request, jsonify
import redis
import uuid
import json
import os

app = Flask(__name__)
redis_client = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=6379, db=0)

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    task_id = str(uuid.uuid4())
    
    task_data = {
        'status': 'pending',
        'length': data['length'],
        'use_digits': data['use_digits'],
        'use_special': data['use_special']
    }
    
    redis_client.set(f"task:{task_id}", json.dumps(task_data))
    redis_client.lpush('password_tasks', task_id)
    
    return jsonify({'task_id': task_id})

@app.route('/api/result/<task_id>', methods=['GET'])
def result(task_id):
    task_data = redis_client.get(f"task:{task_id}")
    if task_data:
        task = json.loads(task_data)
        return jsonify(task)
    return jsonify({'status': 'not_found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
