import time
import visa

rm=visa.ResourceManager()
li=rm.list_resources()
for index in range(len(li)):
    print(str(index)+" - "+li[index])
choice = input("Which device?: ")
vi=rm.open_resource(li[int(choice)])
time.sleep(0.05)

duration = input("Enter minutes to capture: ")
timeout = int(duration)*60 + time.time()
print("timeout= ",duration)
print(time.time())

fn = "c:\\temp\\"+str(time.localtime().tm_year)+"_"+str(time.localtime().tm_mon)+"_"+str(time.localtime().tm_mday)+"_"+str(time.localtime().tm_hour)+"_"+str(time.localtime().tm_min)+".txt"
print("Filename = ",fn)
of = open(fn, 'w')

print(vi.query("*idn?"))
vi.write("func curr:dc ")
vi.write("trig:source int")
time.sleep(0.1)

while time.time() < timeout:
    vi.write("fetch?")
    time.sleep(0.03) # If there are issues, change this time
    curr = vi.read()
    currentTime = str(time.time())
    line = currentTime + " " + str(curr)
    print(line)
    of.write(line)
    time.sleep(0.03) # If there are issues, change this time too
