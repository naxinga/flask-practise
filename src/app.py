from flask import Flask,jsonify,request,json
app = Flask(__name__)

todos = [{ "label" : "my fist task", "done": False}]

@app.route("/todos", methods=["GET"])

def hello_world():

    json_text = jsonify(todos)

    return json_text

@app.route("/todos", methods=["POST"])

def add_new_todo():
    request.get_json(force=True)
    request_body = request.data
    decoded = json.loads(request_body)
    todos.append(decoded)
    json_text = jsonify(todos)
    return json_text

@app.route("/todos/<int:position>", methods=["DELETE"])

def delete_todo(position):
    todos.pop(position)
    json_text = jsonify(todos)
    return json_text

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)