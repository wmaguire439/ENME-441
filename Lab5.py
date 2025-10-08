import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
timeo = time.time()
LED = [2,3,4,17,27,22,10,9,11,5]
f = 0.2

LED_hold = []

n=0
def cb_func(pin):
	global n
	if GPIO.input(21) == HIGH:
		n=1
	else:
		n=-1

GPIO.add_event_detect(21, GPIO.BOTH, callback = cb_func, bouncetime=100)

for i in range(10):
	GPIO.setup(LED[i], GPIO.OUT)
	pwm = GPIO.PWM(LED[i], 500)
	pwm.start(0)
	LED_hold.append(pwm)

while True:
	t = time.time()-timeo
	for i in range(10):
		B = (math.sin(2*math.pi*f-i*n*math.pi/11))**2
		bright = B*100
		LED_hold[i].ChangeDutyCycle(bright)

for i in range(10):
	LED_hold[i].stop()
	GPIO.cleanup()

	

