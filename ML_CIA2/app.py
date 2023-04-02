import pickle
from flask import Flask, request, \
    render_template
app = Flask(__name__)


model = pickle.load(open('model.pkl', 'rb'))


@app.route("/")
def main():
    return render_template("login.html")


@app.route("/predict", methods=['post'])
def pred():
    features = [float(i)
                for i in
                (request.form.values())]
    pred = model.predict([features])
    pred = round(pred[0], 2)
    return render_template("recommend.html",
                           data=pred)


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
