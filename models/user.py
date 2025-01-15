class User:
    def __init__(self, name: str, age: int, username: str, password: str) -> None:
        self.name = name
        self.age = age
        self.username = username
        self.password = password
        
    def getter(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter your age: "))
        self.username = input("Enter Username: ")
        self.password = ("Enter password: ")