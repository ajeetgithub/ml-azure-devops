from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

def model_predict(features):
    """
    Simple mock ML model.
    Calculates weighted sum as prediction.
    """
    weights = np.array([0.5, 1.2, -0.3, 0.8])
    return float(np.dot(features, weights))

@app.route("/")
def home():
    return "ML Prediction API is running."

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = np.array(data["features"])
        prediction = model_predict(features)
        return jsonify({"prediction": round(prediction, 4)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)