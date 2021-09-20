
import paho.mqtt.client as paho
import paho.mqtt.client as mqtt
import random
import sys
import time
import serial
import string
import re
# import time
broker="192.168.43.197"
port=1883
def on_log(client, user_data,level,buf):
    print(buf)
def on_connect(client, user_data, flags,rc):
    if rc == 0:
        client.connected_flag=True
        print ("connected Ok")
    else:
        print ("bad connection = ",rc)
        client.loop_stop()
def on_disconnect(client, user_data,rc):
    print ("Disconnected Ok")
def on_publish(client,userdata,mid):
    print("On_publish message Id",mid)
mqtt.Client.connected_flag=False
client1 = mqtt.Client("control@localhost:1883")
client1.username_pw_set(username="subhajit",password="subhajitsarkar")
#client1.tls_set('/home/pi/mqtt/ssl/ca.crt')
client1.on_log=on_log
client1.on_connect=on_connect
client1.on_disconnect=on_disconnect
client1.on_publish=on_publish
client1.connect(broker,port)
client1.loop_start()
     #connect to broker
# while not client1.connected_flag: #wait in loop
#     print("In wait loop")
#     time.sleep(1)
ser=serial.Serial('/dev/ttyACM0', 115200)
#Here /dev/ttyUSB2 is used
#It can be different in your case like /dev/ttyUSB0, /dev/ttyUSB1 etc.
tim = 5
while True:
    
    line = ser.readline().decode('utf-8').rstrip()
    line1 = re.findall('\d+',line)
    # print(re.findall('\d+',line))
    number = ''.join(x for x in line1 if x.isdigit())
    length = number[0]
    if length[0]== "1":
        sliced = number[1:]
        # print (sliced)
        print(' LDR1_LUX {0} {1}'.format(sliced,"LUX"))
        ret=client1.publish('LDR/LDR1', sliced,2)
        print("published return =",ret)
        # client1.publish('data/value',sliced,qos=0,retain=True)
        time.sleep(tim)
    if length[0]== "2":
        sliced = number[1:]
        # print (sliced)
        print(' LDR2_LUX {0} {1}'.format(sliced,"LUX"))
        ret=client1.publish('LDR/LDR2', sliced,2)
        print("published return =",ret)
        time.sleep(tim)
    if length[0]== "3":
        sliced = number[1:]
        # print (sliced)
        print(' LDR3_LUX {0} {1}'.format(sliced,"LUX"))
        ret=client1.publish('LDR/LDR3', sliced,2)
        print("published return =",ret)
        time.sleep(tim)
    if length[0]== "4":
        sliced = number[1:]
        # print (sliced)
        print(' LDR4_LUX {0} {1}'.format(sliced,"LUX"))
        ret=client1.publish('LDR/LDR4', sliced,2)
        print("published return =",ret)
        time.sleep(tim)
    if length[0]== "5":
        sliced = number[1:]
        # print (sliced)
        print(' LDR5_LUX {0} {1}'.format(sliced,"LUX"))
        ret=client1.publish('LDR/LDR5', sliced,2)
        print("published return =",ret)
        time.sleep(tim)
    if length[0]== "6":
        sliced = number[1:]
        # print (sliced)
        print(' LDR6_LUX {0} {1}'.format(sliced,"LUX"))
        ret=client1.publish('LDR/LDR6', sliced,2)
        print("published return =",ret)
        time.sleep(tim)
    time.sleep(1)
client1.loop_forever()