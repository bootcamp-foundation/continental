import json
from pprint import pprint
from services.authentications import register, login

from models.user import User
from models.book import Book
from models.room import Room
from menu import menu, book_user


def main():
    users: list[User]    = [] 
    rooms: list[Room]    = []
    session: list[User]  = []
    bookings: list[Book] = []
    
    # JSON faylni ochish
    with open("files/rooms.json", "r", encoding="utf-8") as fayl:
        rooms = json.load(fayl)  # JSON ma'lumotni yuklash

    while True:
        menu()
        choose = input("Buyruqni kiriting: ")
        if choose == '1':
            # users listimizga yangi foydalanuvchi qo`shamiz
            users_new = register(users)
            book_user(rooms, users_new)
            print(users_new.name)
            users.append(users_new)
            print(users[0].password)
        elif choose == '2':
            user_booking = login(users)
            if user_booking:
                print("Mexmonnxonaga hush kelibsi! :)")
                # Bu erda bron qilingan xonani saqlaymiz
                bookings.append(book_user(rooms, user_booking))
            else:
                print("Login yoki parol xato!\n")
        elif choose == '3':
            print("Buncha tez ketyabsiz?\n")
            exit()
        else:
            print("Bunday buyrug` mavjud emas, iltimos tekshirib qaytadan kiriting!\n")

main()