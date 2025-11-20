# packages
from menus.main_menu import text_menu
from core.sender import send_request
from core.storage import show_history


def get_command():
    try:
        return int(input("> "))
    except ValueError:
        print("❗ Please enter a valid number.")
        return None


def main():
    print(text_menu)

    while True:
        cmd = get_command()

        if cmd is None:
            continue

        if cmd == 1:
            send_request()
            continue

        elif cmd == 2:
            show_history()
            continue

        elif cmd == 0:
            print("bye!")
            break

        else:
            print("Invalid command! Please choose again.")
            print(text_menu)


if __name__ == "__main__":
    main()
