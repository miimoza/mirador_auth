import RFID
import get_user_info


def main():
    while True:
        print("MIRADOR_AUTH v0.0.1")
        data = RFID.read()
        id = data.get_id()
        pretty_print(get_user_info(id))

main()
