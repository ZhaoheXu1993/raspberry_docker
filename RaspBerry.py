from flask import Flask, render_template
import requests
import threading
import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html',
                           temperature='',
                           humidity='')


def led_controller():
    while True:
        try:
            requests.get('http://ylcktest.ngrok.cc/led/switch/open')
        except:
            print Exception.message
        time.sleep(10)
        try:
            requests.get('http://ylcktest.ngrok.cc/led/switch/close')
        except:
            print Exception.message
        time.sleep(10)


t = threading.Thread(target=led_controller())
t.start()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
