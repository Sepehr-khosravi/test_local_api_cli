#pakages
from menus.main_menu import text_menu
#request package :
from core.sender import send_request

# main menu:
print(text_menu)

while True:
    command = int(input(">"))
    if command == 1:
        send_request()
    elif command == 2:
        pass#keep going here