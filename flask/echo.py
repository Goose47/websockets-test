
from flask import Flask
from flask_uwsgi_websocket import WebSocket

app = Flask(__name__)
ws = WebSocket(app)

@app.route('/')
def index():
    return 'privet'

@ws.route('/echo')
def echo(ws):
    while True:
        msg = ws.receive()
        if msg is not None:
            ws.send(msg)
        else: return