import RPi.GPIO as GPIO

def decimal2binary (value):
    return [int(bit) for bit in format(value, 'b').zfill(8)]
    #return [int(element) for element in bin(value)[2:].zfill(8)]

dac = [10, 9, 11, 5, 6, 13, 19, 26]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try: 
    print("Please, enter the number from 0 to 255: ")
    
    number = input()

    if (not isinstance(number, float)):
        print ("it is not a number")
    
    if (not isinstance(number, int)):
        print("It is not interger")

    number = int(number)

    if (number > 255):
        print ("It is too big")

    if (number < 0):
        print ("It is negative")

    GPIO.output(dac, decimal2binary(number))
    print("The voltage is probably: {:.4f}".format((3.3 * number) / 256))

    print("To finish the program enter q: ")
    s = input()

    if (s == "q"):
        exit()

finally: 
    GPIO.output(dac,0)
    GPIO.cleanup()