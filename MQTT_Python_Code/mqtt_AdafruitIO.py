# Import standard python modules.
import random
import sys
import RPi.GPIO as GPIO
import time
from Adafruit_IO import MQTTClient

GPIO.setmode(GPIO.BCM) 

def random_val(min_val,max_val):
 return random.randint(min_val,max_val)

# Set to your Adafruit IO key.
ADAFRUIT_IO_KEY = 'aio_Bmmo70L3tu3mqwTemePsas1RQ78C'
# Set to your Adafruit IO username.
ADAFRUIT_IO_USERNAME = 'subhajitsarkar91'

def connected(client):
    print('Connected to Adafruit IO!  Listening for changes...')


def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.connect()
client.loop_background()

tim=5
print('Publishing a new message every ' ,time,'seconds (press Ctrl-C to quit)...')
while True:
    LDR1 = random_val(0,1000)
    print(' LDR1_LUX {0} {1}'.format(LDR1,"LUX"))
    client.publish('LDR1', LDR1)
    time.sleep(tim)
    LDR2 = random_val(0,1000)
    print(' LDR2_LUX {0} {1}'.format(LDR2,"LUX"))
    client.publish('LDR2', LDR2)
    time.sleep(tim)
    LDR3= random_val(0,1000)
    print(' LDR3_LUX {0} {1}'.format(LDR3,"LUX"))
    client.publish('LDR3', LDR3)
    time.sleep(tim)
    LDR4 = random_val(0,1000)
    print(' LDR4_LUX {0} {1}'.format(LDR4,"LUX"))
    client.publish('LDR4', LDR4)
    time.sleep(tim)
    LDR5 = random_val(0,1000)
    print(' LDR5_LUX {0} {1}'.format(LDR5,"LUX"))
    client.publish('LDR5', LDR5)
    time.sleep(tim)
    LDR6 = random_val(0,1000)
    print(' LDR6_LUX {0} {1}'.format(LDR6,"LUX"))
    client.publish('LDR6', LDR6)
    time.sleep(tim)


