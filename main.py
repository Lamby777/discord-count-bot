from time import sleep
import pyautogui as auto

DELAY = 0.9

print("Starting number?")
n = int(input())

sleep(3)

while True:
	auto.typewrite(str(n) + " >> ")
	sleep(0.95 * DELAY)

	auto.press("enter")
	n += 1
	sleep(0.05 * DELAY)
