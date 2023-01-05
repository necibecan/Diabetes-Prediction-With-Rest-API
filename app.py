from flask import Flask
from flask import render_template
from flask import request
import numpy as np
import pickle

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/Predict', methods=['POST'])
def Predict():
	pregnanciesNo = request.form.get('pregnanciesNo')
	bldGlucose = request.form.get('bldGlucose')
	bldPressure = request.form.get('bldPressure')
	sknThk = request.form.get('sknThk')
	insulin = request.form.get('insulin')
	bmi = request.form.get('bmi')
	dmPedigreeFunc = request.form.get('dmPredigreeFunc')
	age = request.form.get('age')
	
	resultValues = np.array([[pregnanciesNo, bldGlucose, bldPressure, sknThk, insulin, bmi, dmPedigreeFunc, age]])
	model = pickle.load(open('../Data/model.pkl', 'rb'))
	predictionValue = model.predict(resultValues)

	return render_template('index.html', prediction_text=predictionValue)

if __name__ == 'main':
	app.run(port= 5000, debug=True)

