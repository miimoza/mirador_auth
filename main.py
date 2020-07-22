import RFID.py
import get_user_info


def main():
    print("MIRADOR_AUTH".center())
    exec(open("./MFRC522-python/Read.py").read())
    infos = get_user_info()


main()
