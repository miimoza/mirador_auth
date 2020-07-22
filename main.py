#import RFID
import user
import display
import os
import keyboard
import time

def main():
	os.system('clear')
	while True:
		if keyboard.is_pressed('c'):
			new_id = user.create()
			print("Create new User with ID " + str(new_id))
			time.sleep(3)
			os.system('clear')

		#if keyboard.is_pressed('s'):
		if True:
			#data = "3948328492384239483927584975847"
			data = RFID.read()
			#id = "39"
			id = RFID.get_id(data)
			user.increment_visit(id)
			display.pretty_print(user.get_info(id))
			time.sleep(3)
			os.system('clear')
main()
