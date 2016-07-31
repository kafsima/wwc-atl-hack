add_library('serial')
import StringIO


def setup():
    print Serial.list()
    portIndex = 3
    LF = 10
    myPort = Serial(this, Serial.list()[portIndex], 115200)
    myPort.bufferUntil(LF)



def draw():
    pass
    

def serialEvent(evt):
    input = evt.readString()
    
    with open('/Users/reese/hack/sensor-data/data.txt', 'a') as f:
        f.write(input)