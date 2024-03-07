class Room:

    # Instance attribute
    def __init__(self, name, monster, item, description, connecting_rooms = []):
        self.name = name
        self.monster = monster
        self.item = item
        self.description = description
        self.connecting_rooms = connecting_rooms
     
    def describe_room(self):
            print(self.description)

    def display_room_menu(self):
        print(f"Rommet har {len(self.connecting_rooms)} dører.")
        for i in range(len(self.connecting_rooms)):
            print(f"{i+1}) gå inn i {self.connecting_rooms[i].name}.")
        valg = int(input("Velg fra menyen"))
        return valg-1