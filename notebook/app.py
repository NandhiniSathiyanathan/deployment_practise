from flask import Flask, request_started
import pickle

app = Flask(__name__)

@app.route('/prediction', methods = ['post'])
def preds():
    sl = 'request'.form['sl']
    sw = 'request'.form['sw']
    pl = 'request'.form['pl']
    pw = 'request'.form['pw']

    with open('iris-model.pkl','wb')as f:
     model = pickle.load(f)

    prediction_result = model.predict([[sl,sw,pl,pw]])

    return f"prdicted value is {prediction_result}"

app.run()

    