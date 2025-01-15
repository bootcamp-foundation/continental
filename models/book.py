from .user import User
from .room import Room

class Book:
    def __init__(self, type: str, rooms: int, price: str):
        self.turi = type
        self.xonalari = rooms
        self.narxi = price
