from urllib import response
import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

# def index():
#     return "<h1>Hello World!</h1>"
def index():
    return render_template("index.html")

@app.route('/pokemon/<name>')

def pokemon(name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}').json()
    return render_template("pokemon.html", name=name, id=response["id"], image=response["sprites"]["other"]["official-artwork"]["front_default"])