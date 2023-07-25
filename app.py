from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load the model
model = joblib.load('path_to_your_model.pkl')

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def predict():
    # Get data from POST request
    data = request.get_json()
    
    # Convert data into dataframe
    data = pd.DataFrame(data)
    
    # Make prediction
    cluster = model.predict(data)
    
    # Return results
    return jsonify(cluster.tolist())

if __name__ == '__main__':
    app.run(port=5000, debug=True)
