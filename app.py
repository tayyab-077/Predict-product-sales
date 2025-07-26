from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

# Load model data
model_data = joblib.load("model.pkl")
w = model_data['w']
b = model_data['b']
X_mean = model_data['X_mean']
X_std = model_data['X_std']

# Prediction function
def predict_sales(X_input):
    X_scaled = (X_input - X_mean) / X_std
    return np.dot(X_scaled, w) + b

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = np.array([[float(request.form['TV']),
                              float(request.form['Radio']),
                              float(request.form['Newspaper'])]])
        prediction = predict_sales(features)[0]
        return render_template('index.html', result=f"Predicted Sales: {prediction:.2f}")
    except Exception as e:
        return render_template('index.html', result=f"Error: {e}")

@app.route('/predict_file', methods=['POST'])
def predict_file():
    if 'file' not in request.files:
        return render_template('index.html', result="No file uploaded")

    file = request.files['file']
    try:
        df = pd.read_csv(file)
        X_input = df[['TV', 'Radio', 'Newspaper']].values
        predictions = predict_sales(X_input)
        df['Predicted_Sales'] = predictions
        return render_template('index.html', table=df.to_html(classes='table table-bordered'))
    except Exception as e:
        return render_template('index.html', result=f"Error: {e}")

if __name__ == '__main__':
    
    app.run(debug=True, port=5055) 

