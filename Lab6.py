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

    def __ping(pin):
        """Private method: create a short high pulse on a pin."""
        GPIO.output(pin, 1)
        time.sleep(0)
        GPIO.output(pin, 0)

   def shiftByte(b):
   			GPIO.output(dataPin, b & (1<<i))
			ping(clockPin) # add bit to register
		ping(latchPin) # send register to output

     

# Example usage
if __name__ == "__main__":
    try:
        shifter = Shifter(serialPin=23, clockPin=25, latchPin=24)
        pattern = 0b01100110
        shifter.shiftByte(pattern)

        print("Pattern sent. Press Ctrl+C to exit.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("\nGPIO cleaned up. Exiting.")