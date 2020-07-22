import RFID
import user


def main():
    while True:
        print("MIRADOR_AUTH v0.0.1")

        if "BOUTON PRESSE":
            new_id = user.create()
            print("Create new User with ID " + str(new_id)

        #data = RFID.read()
        data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        id = RFID.get_id(data)
        user.increment_visit(id)
        pretty_print(user.get_info(id))
main()
