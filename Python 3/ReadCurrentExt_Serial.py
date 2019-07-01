import serial
import time

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM5'
ser.timeout = 0.05
print(ser)
ser.open()
print(ser.is_open)

duration = input("Enter minutes to capture: ")
timeout = int(duration)*60 + time.time()
print("timeout= ",duration)
print(time.time())

fn = "c:\\temp\\"+str(time.localtime().tm_year)+"_"+str(time.localtime().tm_mon)+"_"+str(time.localtime().tm_mday)+"_"+str(time.localtime().tm_hour)+"_"+str(time.localtime().tm_min)+".txt"
print("Filename = ",fn)
of = open(fn, 'w')

ser.write("*idn?\n".encode())
print(ser.readline())
ser.write("func curr:dc\n".encode())
#ser.write("trig:source int\n".encode())
time.sleep(0.5)

for i in range(2):
    ser.read()

while time.time() < timeout:
    ser.write("fetch?\n".encode())
    currentTime = str(time.time())
    time.sleep(0.03) # If there are issues, change this time
    curr = ser.readline()
    line = currentTime + " " + curr.decode()
    print(line)
    of.write(line)
    time.sleep(0.03) # If there are issues, change this time too
