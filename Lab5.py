def on():
	n=1

def off();
	n=-1

gpio.add_event_detect(pin_num, gpio.RISING, callback=on, bouncetime=100)
gpio.add_event_detect(pin_num, gpio.FALLING, callback=off, bouncetime=100)


for ()