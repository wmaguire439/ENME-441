import time
import random
from shifter import Shifter
import threading

class Bug:
	__shifter = Shifter(dataPin=23, clockPin=24, latchPin=25)

	def __init__(self, x=3, timestep=0.1, isWrapOn= False):
		self.timestep=timestep
		self.isWrapOn=isWrapOn
		self.__shifter=Bug.__shifter
		self.x=x
		self.begin=False

	def walk(self):
		while self.begin:
			pattern = 1 << self.x
			self.__shifter.shiftByte(pattern)
			led=random.choice([-1,1]) #choose random +1 or -1
			self.x=x+led

			if self.isWrapOn == True:
				if self.x>7:
					self.x=0
				elif self.x<0:
					self.x=7
			if self.isWrapOn == False:
				if self.x>7:
					self.x=7
				elif self.x<0:
					self.x=0

			time.sleep(self.timestep)

	def start(self):
		self.begin = True
		self.thread = threading.Thread(target = self.walk)
		self.thread.start()

	def stop(self)
		self.begin = False
		self.__shifter.shiftByte(0b00000000)

