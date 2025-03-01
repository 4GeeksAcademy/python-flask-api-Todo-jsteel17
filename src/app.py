from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['GET'])
def hello_world():
    return '<h1>Hello!</h1>'

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)

    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    try:
        # Remove the todo at the given position
        deleted_task = todos.pop(position)
        print(f"Deleted task: {deleted_task}")
    except IndexError:
        return jsonify({"error": "Invalid position"}), 400
    
    return jsonify(todos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)