from bug_class import Bug
import RPi.GPIO as GPIO
import time

s1=16
s2=20
s3=21
GPIO.setupmode(GPIO.BCM)
GPIO.setup(s1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

bug = Bug()
s3_hold=0
s2_hold = GPIO.input(s2)

try:
	while True:
		if GPIO.input(s1) == 1:
			bug.start()
		else:
			bug.stop()
		if GPIO.input(s3) == 1 & s3_hold==0:
			bug.timestep = bug.timestep/3
			s3_hold=1
		elif GPIO.input(s3) == 0 & s3_hold==1:
			bug.timestep = 3*bug.timestep
			s3_hold=0
		s2_now = GPIO.input(s2)
		if s2_now != s2_hold:
			if bug.isWrapOn == True:
				bug.isWrapOn = False:
			else:
				bug.isWrapOn = True:

		time.sleep(0.01)

except KeyboardInterrupt:
	GPIO.cleanup()