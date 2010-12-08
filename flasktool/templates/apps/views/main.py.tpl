from flask import Module

main = Module('main')

@main.route('/')
def index():
    return "Win!"

