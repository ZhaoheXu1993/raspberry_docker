from flask import Flask, render_template, request
import controller.led_controller as led_controller
import threading

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    t = threading.Thread(target=led_controller.LEDController().led_blink())
    t.start()
    if request.method == 'POST':
        temperature = request.form.__getattribute__('temperature')
        humidity = request.form.__getattribute__('humidity')
    else:
        temperature, humidity = '', ''
    return render_template('home.html',
                           temperature=temperature,
                           humidity=humidity)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


