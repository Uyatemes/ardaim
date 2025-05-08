from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Разрешаем кросс-доменные запросы

@app.route('/api/sum')
def get_sum():
    try:
        with open('donation_sum.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"current_sum": 0, "target_sum": 5000000})

if __name__ == '__main__':
    app.run(port=5000) 