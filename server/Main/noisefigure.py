import PCF8591 as ADC
import RPi.GPIO as GPIO
import time

num1 = 0
num2 = 0
comp = 0

GPIO.setmode(GPIO.BCM)

def setup():
    ADC.setup(0x48)

def check(voiceValue,count):
    global num1
    global num2
    if count % 2 == 0:
        num1 = voiceValue
    else:
        num2 = voiceValue
        comp = abs (num2 - num1)
        if comp > 0:
            comp = 0
            #print("111")
            return True
        else:
            return False

def loop():
    count = 0
    voiceValue = ADC.read(0)
    if voiceValue:
        print('Value', voiceValue)
        re = check(voiceValue,count)
        if re:
            return True
        else:
            return False
        #if voiceValue < 130:
            #print("111", count)
        count += 1
        time.sleep(0.2)

def main():
    try:
        setup()
        re = loop()
        if re:
            return True
        else:
            return False
    except KeyboardInterrupt:
        pass