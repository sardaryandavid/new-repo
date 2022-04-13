
import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt


dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

def dec2bin(value):
    return [int(bit) for bit in bin(int(value))[2:].zfill(8)]

def bin2dec(list):
    weight = 128
    val = 0
    for i in range(0, 8):
        val += weight * list[i]
        weight /= 2
    
    return val
    
def adc():
    list = [0] * 8
    for i in range(0, 8):
        list[i] = 1
        GPIO.output(dac, list)
        time.sleep(0.001)

        if(GPIO.input(comp) == 0):
            list[i] = 0

    return bin2dec(list)

data = []

try:
    start_time = time.time()

    GPIO.output(17, 1)
    
    val = 0

    while(val <= 255 * 0.9):
        val = adc()
        data.append(val)

        print("Voltage: {:.2f} V".format(val * 3.3 / 256))

        GPIO.output(leds, dec2bin(val))

    endChargeTime = time.time()
    charge_time = endChargeTime - start_time
    
    GPIO.output(17, 0)

    val = 255
    while(val >= 255 * 0.05):
        val = adc()
        data.append(val)
        print("Voltage: {:.2f} V".format(val * 3.3 / 256))
        
        GPIO.output(leds, dec2bin(val))
    
    endDischargeTime = time.time()
    finish_time = endDischargeTime - start_time
        
finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()

plt.plot(data)
plt.show()

data_str = [str(item) for item in data]

with open("7-1_data.txt", "w") as outfile:
    outfile.write("\n".join(data_str))

with open("7-1_settings.txt", "w") as outfile:
    outfile.write("period s\n".format(finish_time / len(data)))
    outfile.write("quant step: {:.5f} V\n".format(3.3 / 256))
    outfile.write("charge time: {:.3f} seconds\n".format(charge_time))
