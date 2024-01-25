
from flask import Flask, render_template
from flask_uwsgi_websocket import WebSocket

app = Flask(__name__)
ws = WebSocket(app)

@app.route('/')
def index():
    return 'prinvefas'

@ws.route('/websocket')
def echo(ws):
    while True:
        msg = ws.receive()
        if msg is not None:
            ws.send(msg)
        else: return

if __name__ == '__main__':
    app.run(debug=True, threads=16)