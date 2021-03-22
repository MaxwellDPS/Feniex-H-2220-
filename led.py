from flask import Flask, render_template
import pifacedigitalio
from time import sleep

app = Flask(__name__)

class LightControl():
    def __init__(self, highwayRelay=0, parkRelay=1):
        self.highwayRelay = highwayRelay
        self.parkRelay = parkRelay
        self.lightBoard = pifacedigitalio.PiFaceDigital()
    def SetRelay(self, Index=0, Set=0, duration=None):
        if not duration:
            self.lightBoard.leds[Index].value = Set
        else:
            set2 = 1 if Set == 0 else 0
            self.lightBoard.leds[Index].value = Set
            sleep(duration)          
            self.lightBoard.leds[Index].value = set2
    def park(self):
        self.SetRelay(self.highwayRelay, 0)
        self.SetRelay(self.parkRelay, 1)
    def highway(self):
        self.SetRelay(self.parkRelay, 0)
        self.SetRelay(self.highwayRelay, 1)
    def off(self):
        self.SetRelay(self.highwayRelay, 0)
        self.SetRelay(self.parkRelay, 0)

Lights = LightControl()

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/highway')
def highway():
    Lights.highway()
    return "SUCCESS"

@app.route('/park')
def park():
    Lights.park()
    return "SUCCESS"

@app.route('/off')
def off():
    Lights.off()
    return "SUCCESS"


if __name__ == '__main__':
   app.run(host='0.0.0.0')