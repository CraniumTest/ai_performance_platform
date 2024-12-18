from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/upload_data', methods=['POST'])
def upload_data():
    try:
        data = request.get_json()
        df = pd.DataFrame(data)
        # Save or process your data
        return jsonify({"message": "Data received successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
