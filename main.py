import RFID
import user
import display


def main():
	while True:
		print("MIRADOR_AUTH v0.0.1")

		if "BOUTON PRESSE":
			new_id = user.create()
			print("Create new User with ID " + str(new_id))
		#data = RFID.read()
		data = "3948328492384239483927584975847"
		id = RFID.get_id(data)
		user.increment_visit(id)
		display.pretty_print(user.get_info(id))
main()
