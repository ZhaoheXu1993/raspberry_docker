from flask import Flask, render_template, request
from flask.ext.cors import CORS
#import controller.led_controller as led_controller
#import threading
import requests
import json
import time

app = Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

data_dict = []


@app.route('/')
def hello_world():
    #t = threading.Thread(target=led_controller.LEDController().led_blink())
    #t.start()
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
