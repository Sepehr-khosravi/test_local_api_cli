import json
import ast
import os

from menus.history_menu import text_history_menu

# path to JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR, "../data/history.json")


def _ensure_file():
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump({}, f)


def add_new_data(new_data):
    try:
        _ensure_file()

        # خواندن دیتا
        with open(path, "r") as f:
            data = json.load(f)

        if not isinstance(data, dict):
            data = {}

        next_id = str(len(data) + 1)
        data[next_id] = new_data

        with open(path, "w") as f:
            json.dump(data, f, indent=4)

    except Exception as e:
        print("error in add_new_data into this path:", path)
        print("details:", e)


def show_history():
    print(text_history_menu)

    try:
        _ensure_file()

        with open(path, "r") as f:
            data = json.load(f)

        # نمایش تاریخچه
        if not data:
            print("History is empty.")
        else:
            for key, item in data.items():
                print(f"[{key}] {item}")

    except Exception as e:
        print("error in show_history from storage.py!")
        print("details:", e)
