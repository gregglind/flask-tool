from flask import Module

api = Module('api', prefix='/api/v1')

@api.route('/')
def index():
    return "API index."
