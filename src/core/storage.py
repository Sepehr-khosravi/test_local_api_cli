#json package for managing json files:
import json

#package
from menus.history_menu import text_history_menu

#path file
path = "../data/history.json"

def add_new_data(new_data):
    #read data file
    try:
      with open(path, "r") as f:
          data = json.load(f)
      #update data file
      data[str(len(data) + 1)] = new_data
      with open(path, "w") as f:
          json.dump(data, f, indent=4)
    except:
        print("error in add_new_data into this path : " , path)

def show_history():
    print(text_history_menu)
    try:
        with open(path, "r") as f:
            data = json.load(f)
        print(data)
    except:
        print("error in show_history from storage.py! ")