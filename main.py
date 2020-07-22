import RFID
import user


def main():
    while True:
        print("MIRADOR_AUTH v0.0.1")
        #data = RFID.read()
        if "BOUTON PRESSE":
            new_id = create_user()
            print("Create new User with ID " + new_id)

        data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        id = RFID.get_id(data)
        pretty_print(get_user_info(id))
main()
