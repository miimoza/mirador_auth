import RFID
import get_user_info


def main():
    while True:
        print("MIRADOR_AUTH".center())
        exec(open("./MFRC522-python/Read.py").read())
        pretty_print(get_user_info())

main()
