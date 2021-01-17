import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('./random_model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():

    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    
    prediction = model.predict(final_features)

    output =prediction[0]
    print(output)
    return render_template('index.html', prediction_text='${}'.format(output))
if __name__ == "__main__":
    app.run(debug=True)