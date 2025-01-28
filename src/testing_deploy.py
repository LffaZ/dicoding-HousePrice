from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
joblib_model = joblib.load('models/gbr_model.joblib') # Pastikan path file sesuai dengan penyimpanan Anda

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json.get('data', None)  # Mengambil data dari request JSON
    
    if not data:
        return jsonify({"error": "Data not found in request"}), 400
    
    # Validasi apakah data berupa list of lists
    if not isinstance(data, list) or not all(isinstance(i, list) for i in data):
        return jsonify({"error": "Data should be a 2D array"}), 400

    try:
        prediction = joblib_model.predict(data)  # Melakukan prediksi
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)

# command: Invoke-RestMethod -Uri "http://127.0.0.1:5000/predict" -Method Post -Headers @{ "Content-Type" = "application/json" } -Body (Get-Content -Raw -Path "data.json")