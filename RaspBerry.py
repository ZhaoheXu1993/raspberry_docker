from flask import Flask, render_template
import requests
import threading
import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')


def led_controller():
    while True:
        requests.get('http://9d542a1b.ngrok.io/led/switch/open')
        time.sleep(10)
        requests.get('http://9d542a1b.ngrok.io/led/switch/close')
        time.sleep(10)


t = threading.Thread(target=led_controller())
t.start()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
