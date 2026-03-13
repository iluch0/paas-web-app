from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Aplicación desplegada en PaaS correctamente"

@app.route("/info")
def info():
    return f"Variable de entorno: {os.getenv('MENSAJE')}"

if __name__ == "__main__":
    app.run()