from app import app
from app import websocket


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