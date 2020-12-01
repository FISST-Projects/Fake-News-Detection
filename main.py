#main.py
import sys
sys.path.append('localpackage')
import localpackage.nltk as nltk
nltk.data.path.append('localpackage/nltk_data/')

from flask import Flask, jsonify, request, render_template
from predictor import predict

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def output():
    try:
        json =request.get_json()
        input_text = json["text"]
        return predict(input_text)
    except Exception as e:
        return f"An error Occured: {e}"


@app.route('/')
def hello_name():
   return render_template('index.html')

if __name__ == '__main__':
    app.run()
