from flask import Flask, render_template
import controller.led_controller as led_controller
import threading

app = Flask(__name__)


@app.route('/')
def hello_world():
    t = threading.Thread(target=led_controller.LEDController().led_blink())
    t.start()
    return render_template('home.html',
                           temperature='',
                           humidity='')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


