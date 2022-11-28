from flask import Flask


signal_interpreter_app=Flask(__name__)

@signal_interpreter_app.route("/", methods=["POST"])
def index():
    return "Hello World"

