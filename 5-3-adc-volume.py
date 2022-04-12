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

leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(leds, GPIO.OUT)

try:
    while True:
        
        value = 0
        
        for n in range (8): 
            value += int(2 ** (7 - n))

            signal = dec2bin(value)
            GPIO.output (dac, signal)
            time.sleep(0.001)
            
            compVal = adc ()

            if (compVal == 0):
                value -= 2 ** (7 - n)

        voltage = value / 256 * maxVoltage

        light = voltage * 8 // 256

        GPIO.output(leds[:light], 1)
        GPIO.output(leds[light:], 0)

        print("value: ", value, "signal:", signal,"The voltage is ", voltage)

        GPIO.output (leds, GPIO.input(dac))

finally:
    GPIO.output(dac,GPIO.LOW)
    GPIO.cleanup()