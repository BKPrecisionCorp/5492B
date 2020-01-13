import serial
import time

ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/ttyUSB1'
ser.timeout = 0.1
print(ser)
ser.open()
print(ser.is_open)

ser.write(b'*idn?\n') # Read the ID
print(ser.read_until("\n"))

#Setup the function and trigger
ser.write(b'func volt:ac\n')
time.sleep(0.1)
ser.write(b'trig:source ext\n')
ser.write(b'trig:source?\n')
print(ser.read_until("\n"))
time.sleep(3)
ser.write(b'data?\n')
print(ser.read_until("\n"))

