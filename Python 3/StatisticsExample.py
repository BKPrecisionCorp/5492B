import time
import visa
rm=visa.ResourceManager()
li=rm.list_resources()
for index in range(len(li)):
    print(str(index)+" - "+li[index])
choice = input("Which device?: ")
vi=rm.open_resource(li[int(choice)])
time.sleep(0.05)

print(vi.query("*idn?"))
vi.write("func res ")
vi.write("trig:source bus")
vi.write("calc2:state 1")
vi.write("calc2:trace:points 10")
vi.write("calc2:trace:cle")
print("state= ", vi.query("calc2:state?"))

for i in range(10):
    msg = "Point " + str(i+1) + " press enter"
    print(msg)
    input()
    vi.write("*trg")

print("State now: ", vi.query("calc2:state?"))
vi.write("calc2:state 1")
print("Data= ", vi.query("calc2:trace:data?"))
print("Data= ", vi.query("calc2:trace:data?"))
vi.write("calc2:format max")
print("Max=", vi.query("calc2:imm?"))
vi.write("calc2:format min")
print("Min=", vi.query("calc2:imm?"))
vi.write("calc2:format mean")
print("Mean=", vi.query("calc2:imm?"))
vi.write("calc2:format sedv")
print("SEDV=", vi.query("calc2:imm?"))
print("Data= ", vi.query("calc2:trace:data?"))
vi.write("calc2:state 0")
