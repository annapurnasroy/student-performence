from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# load model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form

    try:
        input_dict = {
            'Student_Age': int(data['Student_Age']),
            'Sex': data['Sex'],
            'High_School_Type': data['High_School_Type'],
            'Scholarship': int(data['Scholarship']),
            'Additional_Work': data['Additional_Work'],
            'Sports_activity': data['Sports_activity'],
            'Transportation': data['Transportation'],
            'Weekly_Study_Hours': int(data['Weekly_Study_Hours']),
            'Attendance': data['Attendance'],
            'Reading': data['Reading'],
            'Notes': data['Notes'],
            'Listening_in_Class': data['Listening_in_Class'],
            'Project_work': data['Project_work']
        }

        df = pd.DataFrame([input_dict])

        prediction = model.predict(df)[0]

        return render_template('index.html', prediction_text=f'Predicted Grade: {prediction}')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)