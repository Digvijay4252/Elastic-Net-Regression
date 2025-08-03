from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load model and encoders
model = joblib.load('model.pkl')
encoders = joblib.load('encoders.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            age = int(request.form['age'])
            sex = request.form['sex']
            bmi = float(request.form['bmi'])
            children = int(request.form['children'])
            smoker = request.form['smoker']
            region = request.form['region']

            # Encode categorical features
            sex_enc = encoders['sex'].transform([sex])[0]
            smoker_enc = encoders['smoker'].transform([smoker])[0]
            region_enc = encoders['region'].transform([region])[0]

            # Prepare features and predict
            features = [[age, sex_enc, bmi, children, smoker_enc, region_enc]]
            pred = model.predict(features)[0]
            prediction = f"${pred:,.2f}"

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
