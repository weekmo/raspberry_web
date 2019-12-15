from flask import Flask, render_template, request
import RPi.GPIO as GPIO

#GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
#GPIO.setup(7,GPIO.OUT)

app = Flask(__name__)

btns = {
    3:"Light 1",
    5:"Fan",
    7:"Light 3",
    11:"Light 4",
}

for i in btns:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,True)

@app.route('/')
def index():
    # run RaspberryPi
    return render_template('index.html', btns=btns)

@app.route('/checked/', methods=['POST'])
def checked():
    btn_id = int(request.form['id'])
    GPIO.output(btn_id,False)
    return btns[btn_id] +" turned on successfully"

@app.route('/unchecked/', methods=['POST'])
def unchecked():
    btn_id = int(request.form['id'])
    GPIO.output(btn_id,True)
    return btns[btn_id] +" turned off successfully"

try:
    if __name__ == "__main__":
        app.run(debug=True,host="0.0.0.0",port=80)
except:
    GPIO.cleanup()
    print("Error !")

finally:
    for i in btns:
        GPIO.output(i,True)
