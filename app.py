import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

# load pickle file
with open("./boston-model/linear_regression_model.pkl", "rb") as f:
    model = pickle.load(f)

# load pickle scaler file
with open("./boston-model/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Try to get JSON data first
    if request.is_json:
        data = request.get_json()
        features = data.get("features")
    else:
        # Parse form data
        features = []
        feature_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
        for name in feature_names:
            value = request.form.get(name)
            if value is None or value == '':
                return jsonify({"error": f"Missing value for {name}"}), 400
            features.append(float(value))

    # Validate for missing values in JSON
    if features is None or any(f is None or f == '' for f in features):
        return jsonify({"error": "Missing one or more feature values."}), 400

    features = [float(f) for f in features]
    features = np.array(features).reshape(1, -1)
    features = scaler.transform(features)
    prediction = model.predict(features)
    return render_template("index.html", prediction=round(prediction[0], 2))

if __name__ == "__main__":
    app.run(debug=True)