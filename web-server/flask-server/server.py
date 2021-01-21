from flask import Flask

app = Flask(__name__)
# print(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

# Installation - Windows Powershell
# cd web-server
# py -3 -m venv flask
# venv\Scripts\activate.ps1
# pip --version
# pip3 --version
# pip3 install Flask
# c:\users\asus\appdata\local\programs\python\python39\python.exe -m pip
#  install --upgrade pip
# pip3 install --upgrade pip
# pip install --upgrade pip

# Run Server - Windows Powershell
# cd flask-server
# $env:FLASK_APP = "server.py"
# $env:FLASK_ENV = "development"
# flask run
