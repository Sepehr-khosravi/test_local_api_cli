#pakages
from menus.main_menu import text_menu
#request package :
from core.sender import send_request
from core.storage import show_history

# main menu:
print(text_menu)

while True:
    command = int(input(">"))
    if command == 1:
        send_request()
    elif command == 2:
        show_history()
    elif command == 0:
        print("bye!")
        break
    else :
        print("bye!")
        break