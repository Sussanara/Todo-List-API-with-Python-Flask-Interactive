from flask import Flask, jsonify, request, json

app = Flask(__name__)

todos = [
    { "label": "Terminar este trabajo", "done": False },
    { "label": "Tomar cafecito", "done": False }
]
@app.route('/')
def nothing():
    return 'nothing here, proceed to /todos'

@app.route('/todos', methods=['GET'])
def hello_world():
    
    json_object = jsonify(todos)
    
    return json_object

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    to_append = json.loads(request_body)
    print("Incoming request with the following body", request_body)
    todos.append(to_append)
    return jsonify(todos)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)