```python
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

researchers = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    researchers[data['username']] = data
    return jsonify({'message': 'Registered successfully'}), 200

@socketio.on('share_findings')
def handle_share_findings(data):
    findings = data['findings']
    username = data['username']
    researchers[username]['findings'] = findings
    emit('findings_updated', {'username': username, 'findings': findings}, broadcast=True)

@socketio.on('contribute_model')
def handle_contribute_model(data):
    model = data['model']
    username = data['username']
    researchers[username]['model'] = model
    emit('model_updated', {'username': username, 'model': model}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
```