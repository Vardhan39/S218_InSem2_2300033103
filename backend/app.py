from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample quiz data
quizzes = []

@app.route('/api/quizzes', methods=['GET'])
def get_quizzes():
    return jsonify(quizzes)

@app.route('/api/quizzes', methods=['POST'])
def create_quiz():
    quiz = request.json
    quizzes.append(quiz)
    return jsonify(quiz), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)