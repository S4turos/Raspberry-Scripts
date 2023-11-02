import RPi.GPIO as GPIO
import time
import subprocess
import os

script_dir = os.path.dirname(__file__)
gpuFile = os.path.join(script_dir, 'gpuTemp.sh')
cpuFile = os.path.join(script_dir, 'cpuTemp.sh')
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
fan = GPIO.PWM(8, 100)
fan.start(0)

def checkGPU():
	proc = subprocess.check_output(gpuFile)
	temp = float(proc)
	return temp

def checkCPU():
	proc = subprocess.check_output(cpuFile)
	temp = float(int(proc)/1000)
	return temp

while True:
	gpu = checkGPU()
	cpu = checkCPU()
	if cpu > gpu:
		max = cpu
	elif gpu > cpu:
		max = gpu
	else:
		max = cpu

	if max >= 70.0 and max < 75.0:
		fan.ChangeDutyCycle(80)
	elif max >= 75.0:
		fan.ChangeDutyCycle(100)
	else:
		fan.ChangeDutyCycle(0)

	time.sleep(15)

