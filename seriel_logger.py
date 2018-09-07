import serial
import time
import datetime

ser = serial.Serial(
    port='/dev/asdfasdf',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0)

print("connected to: " + ser.portstr)

while True:
    line = ser.readline()
    timestamp = str(time.time())
    #timestamp = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    with open('output.txt', 'a') as pyfile:
        pyfile.write(line + ' ' + timestamp +'\n')
        
ser.close()








