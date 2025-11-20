#pakages:
from menus.request_menu import text_menu_request
from storage import add_new_data
import requests


#last data
import json
    
path_last_data_file = "../data/last_data.json"
def load_data():
    try:
      with open(path_last_data_file, "r") as f:
          return json.load(f)
    except :
        print("error in load_data from sender.py in this path : " , path_last_data_file)
    

def send_request(url = "", method = "", headers = "" ):
    print(text_menu_request)
    #load data
    try:
      data = load_data()
      #if data wasn't exists:
      if not data:
          url = input("please set your url : ")
          method = input("please set your method(GET, POST, PUT, PATCH, DELETE) : ")
          if not method == "GET":
              body = input("please set your body data : ")
          headers = input("please set your headers : ")
      else :
          url = data["url"]
          method = data["method"]
          if(not method == "GET"):
              body = data["body"]
          headers = data["headers"]
      #send request
      if method == 1:
          response = requests.get(url=url, headers=headers )
      elif method == 2:
          response = requests.post(url=url, json=body, headers=headers)
      elif method == 3:
          response = requests.put(url=url, json=body, headers=headers )
      elif method == 4:
          response = requests.patch(url=url , json=body, headers=headers)
      elif method == 5:
          response = requests.delete(url=url, json=body, headers=headers)
      else : 
          print("method must be one of them : (GET, POST, PUT, PATCH, DELETE)")
      #saving new data in last_data.json
      new_data = {
          "url" : url,
          "method" : method,
          "body" : body,
          "headers" : headers 
      }
  
      with open(path_last_data_file, "w") as f:
          json.dump(new_data, f, indent=4)
      #for adding saved-requests too
      add_new_data(new_data=new_data)
      return response
    except:
        print("error in send_request from sender.py!")

