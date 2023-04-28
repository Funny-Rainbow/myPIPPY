import sys
from time import sleep
from socketTransfer import socketTransfer

def shabi():
    tfile=open("/sys/bus/w1/devices/28-01205a8a3a8d/w1_slave")
    print("before read")
    text = tfile.read()
    print("after read")
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    temperature = temperature / 1000
    socketTransfer(str(temperature))
    return temperature

if __name__ == '__main__':
    while(1):
        sleep(5)
        #data = input()
        print(shabi())