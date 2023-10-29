from flask import Flask, request, jsonify
import pickle
import numpy as np
from waitress import serve
from joblib import load
import sklearn

app = Flask(__name__)

# Load the logistic regression model
dt_classifier = load('model.bin')

# Load the DictVectorizer
dict_vectorizer = load('dv.bin')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json() # Get data from user 
        client_data_transformed = dict_vectorizer.transform([data]) # Encode categorical features
        probability = dt_classifier.predict_proba(client_data_transformed)
        churn_probability = probability[0][1] # Return probability
        return jsonify({'probability': churn_probability})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8081)
