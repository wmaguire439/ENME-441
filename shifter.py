import RPi.GPIO as GPIO
import time

class Shifter:
    def __init__(self, serialPin, clockPin, latchPin):
        # Store pin assignments as class attributes
        self.serialPin = serialPin
        self.clockPin = clockPin
        self.latchPin = latchPin

        # GPIO setup
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.serialPin, GPIO.OUT)
        GPIO.setup(self.clockPin, GPIO.OUT)
        GPIO.setup(self.latchPin, GPIO.OUT)

    def __ping(self, pin):
        """Private method: create a short high pulse on a pin."""
        GPIO.output(pin, 1)
        time.sleep(0)
        GPIO.output(pin, 0)

   def shiftByte(self, pattern):
   		for i in range(8):
   			GPIO.output(self.dataPin, pattern & (1<<i))
			GPIO.output(self.clockPin, 1)
        	time.sleep(0)
       		GPIO.output(self.clockPin, 0) # add bit to register
		GPIO.output(self.latchPin, 1)
        time.sleep(0)
       	GPIO.output(self.latchPin, 0) # send register to output

     