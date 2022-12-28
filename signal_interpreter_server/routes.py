from flask import Flask
from signal_interpreter_server.json_parser import JsonParser


signal_interpreter_app=Flask(__name__)
json_parser=JsonParser()

@signal_interpreter_app.route("/", methods=["POST"])
def index():
    return "Hello World"

