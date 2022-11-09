from time import sleep
import pyautogui as auto

DELAY = 0.04

print("Starting number?")
n = int(input())

sleep(3)

while True:
	auto.typewrite(str(n))
	sleep(DELAY)

	auto.press("enter")
	n += 1
	sleep(DELAY)

