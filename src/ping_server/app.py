from flask import Flask, request
import threading
import os
from time import time, sleep
import json

app = Flask(__name__)

def save_data(data):
    with open("src/ping_server/computers.json", "w") as f:
        json.dump(data, f, indent=2)

def call_em():
    print("Oh no server is down!")

def call_dog():
    while True:
        with open("src/ping_server/computers.json") as f:
            data = json.load(f)

        for computer in data["whitelisted"]:
            if time() - data[computer]["last_seen"] > 5 and  not data[computer]["notified"]:
                call_em()
                data[computer]["notified"] = True
                save_data(data)

        sleep(5)


@app.route("/alive/<computer>", methods=["POST"])
def ping(computer):
    with open("src/ping_server/computers.json") as f: data = json.load(f)
    if computer not in data["whitelisted"]: return "sowwy, you not allowed", 403

    if computer not in data: 
        data[computer] = {"last_seen": time(), "notified": False}
        save_data(data)
        return "Added you <3", 201
    
    data[computer]["last_seen"] = time()
    save_data(data)
    return "Thanks for the update!", 200 


        
if __name__ == "__main__":
    threading.Thread(target=call_dog, daemon=True).start()
    app.run(host="0.0.0.0")