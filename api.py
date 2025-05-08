from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Разрешаем кросс-доменные запросы

@app.route('/api/sum', methods=['GET', 'POST'])
def get_or_update_sum():
    if request.method == 'POST':
        data = request.get_json()
        current_sum = data.get('current_sum', 0)
        target_sum = data.get('target_sum', 5000000)
        with open('donation_sum.json', 'w') as f:
            json.dump({'current_sum': current_sum, 'target_sum': target_sum}, f)
        return jsonify({'current_sum': current_sum, 'target_sum': target_sum})
    else:
        try:
            with open('donation_sum.json', 'r') as f:
                data = json.load(f)
            return jsonify(data)
        except FileNotFoundError:
            return jsonify({"current_sum": 0, "target_sum": 5000000})

if __name__ == '__main__':
    app.run(port=5000) 