from flask import Flask, request, jsonify, render_template, make_response

app = Flask('{{app.name}}')

@app.route('/')
def index():
    return render_template('index.html')