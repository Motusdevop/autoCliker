import time

import keyboard
import mouse

run = False

def set_cliker():
	global run
	if run:
		run = False
	else:
		run = True


keyboard.add_hotkey("Alt + Z", set_cliker)

while True:
	if run:
		mouse.double_click(button = "left")
		time.sleep(0.001)