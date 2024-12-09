from flask import Flask, render_template
from flask_jsonrpc import JSONRPC

app = Flask(__name__)
jsonrpc = JSONRPC(app, "/api")  # Ruta donde estará disponible el servidor JSON-RPC

@app.route('/')
def home():
    return render_template('index.html', ViewData={"Title": "Aplicacion Web 2"})


@jsonrpc.method('App.hello_world')
def hello_world() -> str:  # Especificamos explícitamente el tipo de retorno como str
    return "Hola, mundo desde RPC"


@jsonrpc.method('App.add_numbers')
def add_numbers(num1: int, num2: int) -> int:
    return num1 + num2

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)