import RPi.GPIO as GPIO
import time

def dec2bin (value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

def num2dac (val):
    signal = dec2bin(val)
    GPIO.output (dac, signal)
    return signal 

def adc (): 
    compValue = GPIO.input (comp)
    return compValue

maxVoltage = 3.3

dac = [26, 19, 13, 6, 5, 11, 9, 10]

comp = 4
troyka = 17
maxVoltage = 3.3
bits = len(dac)
levels = 2 ** bits

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

signalList = [1, 0, 0 , 0, 0, 0, 0, 0]

try:
    while True:
        
        value = 0
        
        for n in range (8): 
            value += int(2 ** (7 - n))

            signal = dec2bin(value)
            GPIO.output (dac, signal)
            time.sleep(0.001)
            voltage = value /255 * maxVoltage

            compVal = adc ()

            if (compVal == 0):
                value -= 2 ** (7 - n)

        print("value: ", value, "signal:", signal,"The voltage is ", voltage)

finally:
    GPIO.output(dac,GPIO.LOW)
    GPIO.cleanup()