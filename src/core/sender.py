# packages:
from menus.request_menu import text_menu_request
from core.storage import add_new_data
import requests
import json
import ast
import os

# path to JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path_last_data_file = os.path.join(BASE_DIR, "../data/last_data.json")

def load_data():
    try:
        if not os.path.exists(path_last_data_file):
            return None
        
        with open(path_last_data_file, "r") as f:
            content = f.read().strip()
            if content == "":
                return None
            return json.loads(content)
    except Exception as e:
        print("❌ Error loading last_data.json:", e)
        return None
    

def send_request():
    print(text_menu_request)

    data = load_data()

    # --- Get Inputs ---
    if not data:
        url = input("URL: ").strip()
        method = input("Method (GET, POST, PUT, PATCH, DELETE): ").upper().strip()

        body = None
        if method != "GET":
            print("Body (dict format e.g. {\"name\": \"ali\"}): ")
            raw_body = input("> ")
            try:
                body = ast.literal_eval(raw_body)  # convert string → dict
            except:
                body = {}
        
        print("Headers (dict format e.g. {\"Authorization\": \"Bearer xyz\"}):")
        raw_headers = input("> ")
        try:
            headers = ast.literal_eval(raw_headers)
        except:
            headers = {}

    else:
        url = data.get("url", "")
        method = data.get("method", "GET").upper()
        body = data.get("body", None)
        headers = data.get("headers", {})

    # --- Validate Method ---
    valid_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    if method not in valid_methods:
        print("❌ method must be one of:", valid_methods)
        return

    # --- Send Request ---
    try:
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, json=body, headers=headers)
        elif method == "PUT":
            response = requests.put(url, json=body, headers=headers)
        elif method == "PATCH":
            response = requests.patch(url, json=body, headers=headers)
        elif method == "DELETE":
            response = requests.delete(url, json=body, headers=headers)
    except Exception as e:
        print("❌ Request failed:", e)
        return

    # --- Save last_data ---
    new_data = {
        "url": url,
        "method": method,
        "body": body,
        "headers": headers
    }

    try:
        with open(path_last_data_file, "w") as f:
            json.dump(new_data, f, indent=4)
    except Exception as e:
        print("❌ Error writing last_data.json:", e)

    # --- Save to saved-requests ---
    try:
        add_new_data(new_data=new_data)
    except Exception as e:
        print("❌ Error saving request history:", e)

    return response
