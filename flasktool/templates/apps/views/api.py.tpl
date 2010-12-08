from flask import Module

api = Module(__name__, url_prefix='/api/v1')

@api.route('/')
def index():
    return "API index."
