from app import app
from flask_uwsgi_websocket import GeventWebSocket


websocket = GeventWebSocket()
websocket.init_app(app)

# a list to store all connected clients
clients = []
# sample websocket endpoint
@websocket.route('/echo')
def echo(ws):
    clients.append(ws)
    while True:
        msg = ws.receive()
        ws.send(msg)
        time.sleep(0.5)


@app.route('/')
def home():
   return "hello world!"