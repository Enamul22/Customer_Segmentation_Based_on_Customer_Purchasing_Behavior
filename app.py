from flask import Flask, request, render_template
from joblib import load

app = Flask(__name__)
model = load('/Users/enamul/Desktop/Data Science Projects/Customer Segmentation/model/cs_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        data = request.form
        recency = float(data['recency'])
        frequency = float(data['frequency'])
        monetary_value = float(data['monetary_value'])
        prediction = model.predict([[recency, frequency, monetary_value]])[0]
        return render_template('index.html', prediction=prediction)
    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)