from flask import Flask, request, jsonify
from validator import evaluate_state

app = Flask(__name__)

@app.route('/v1/state/evaluate', methods=['POST'])
def evaluate():
    data = request.json
    result = evaluate_state(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
