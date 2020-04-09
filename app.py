from flask import Flask, request, jsonify, render_template
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_cors import CORS
from models import db
from myqueue import Queue


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
CORS(app)
Migrate(app, db)

manager = Manager(app)
manager.add_command("db", MigrateCommand)

@app.route("/")
def main():
    return render_template("index.html")

# if method == GET va a usar self._queue y manda mensaje
# if method == GET (all) mostrat arreglo self.queue
# if method == POST

@app.route("/new", methods=["POST"])# recibe a 1 y llama a next
def new_element():
    queue = Queue() # trae las funciones de la clase queue de myqueue.py
    item = request.json.get("item") # elegir q persona agregar a la lista
    queue.enqueue(item) # se ejecuta la funcion y se va a agregar los elementos a la lista y se va a mandar un mensaje
    return jsonify({"msj" : "mensaje enviado"}) # si se ejecuta correctamente se manda el mensaje

#este lo hice yo, REVISAR
@app.route("/next", methods=["GET"])# la persona avanza y le llega un mensaje
def next_element():
    queue = Queue() # trae las funciones de la clase queue de myqueue.py
    item = request._queue.pop("item")
    queue.dequeue(item)
    return jsonify({"msj" : "mensaje enviado"}) # si se ejecuta correctamente se manda el mensaje
    
#este lo hice yo, REVISAR
@app.route("/all", methods=["GET"]) #muestra la persona en la lista o en espera
def all_element():
    queue = Queue() # trae las funciones de la clase queue de myqueue.py
    queue.json.get(item)

if __name__ == "__main__":
    manager.run()