# ------------ imports ------------
import os
from weapon import Weapon
from character import Character
from room import Room

# ------------ setup ------------

current_room = None

# Lager våpen
fists = Weapon("Fists", "blunt", 2, 0)
iron_sword = Weapon("Iron Sword", "sharp", 5, 10)
short_bow = Weapon("Short Bow", "ranged", 4, 8)



# lager spiller og monster
helt = Character("Erik", 100, fists)
monster_kjøkken = Character("Kjøkkenmonster", 50, fists)
monster_storsal = Character("Storsalmonster", 200, short_bow)

# Lager rom og legger inn monstre og gjenstander
start_rom = Room("Start", None, None, "Du står i en mørk kjeller.")
kjøkken = Room("Kjøkken", monster_kjøkken, short_bow, "Kjøkkenet. Det stinker her.")
siderom = Room("Siderom", None, iron_sword, "Et lite kott med støv")
storsal = Room("Storsal", monster_storsal, iron_sword, "En gigantisk sal. Her var det sikkert ball og store fester, før veggene ble neddynket med blod.")
nytt_rom = Room("Nyhet", monster_storsal, iron_sword, "Det nye rommet.")


# Kobler rommene sammen
start_rom.connecting_rooms = [kjøkken, storsal, nytt_rom]
kjøkken.connecting_rooms = [start_rom, siderom]
siderom.connecting_rooms = [kjøkken]
storsal.connecting_rooms = [start_rom]
nytt_rom.connecting_rooms = [start_rom]


current_room = start_rom
# ------------ game loop ------------
while True:
    os.system("cls")

    current_room.describe_room()
    neste_rom = current_room.display_room_menu()
    current_room = current_room.connecting_rooms[int(neste_rom)]

    #input("Trykk en tast for å fortsette")

