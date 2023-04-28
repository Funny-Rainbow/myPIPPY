import sys
from time import sleep

def shabi():
    tfile=open("/sys/bus/w1/devices/28-01205a8a3a8d/w1_slave")
    text = tfile.read()
    tfile.close
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    temperature = temperature / 1000
    return temperature


if __name__ == '__main__':
    while(1):
        #data = input()
        print(tempe())
        sleep(0.1)