#Keep Running
from s import run
from flask import Flask
from threading import Thread

app = Flask('')

t = Thread(target=run)
t.start()

@app.route('/')
def home():
    return "Online."

app.run(host='0.0.0.0',port=8080)
