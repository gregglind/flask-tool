from flask import Module, render_template, current_app, g, session

main = Module(__name__)

@main.route('/')
def index():
    return render_template('index.html')

