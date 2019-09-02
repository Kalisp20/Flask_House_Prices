import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn import preprocessing

app = Flask(__name__)
model = pickle.load(open('house_price_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    print('INT OK')
    print('Int='%int_features)
    
    print('final en cours')
    final_features = np.array(int_features)
    final_features= final_features.reshape(1,-1)
    print(final_features.shape)

    print('Prédiction en cours')
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='House price should be $ {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    print(output)
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)