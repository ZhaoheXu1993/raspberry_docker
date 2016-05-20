from flask import Flask, render_template
import requests
import json
import time

app = Flask(__name__)

data_dict = []


@app.route('/')
def hello_world():
    return render_template('home.html',
                           temperature='',
                           humidity='')


@app.route('/show')
def show():
    current_time = time.strftime('%m-%d %H:%M:%S', time.localtime())
    response = requests.get('http://ylcktest.ngrok.cc/temperandhumidity')
    data = json.loads(response.text)
    data_dict.append({'current_time': current_time,
                      'temperature': data['temperature'],
                      'humidity': data['humidity']})
    return render_template('home.html',
                           dicts=data_dict)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
