from flask import Flask
from flask_uwsgi_websocket import GeventWebSocket
app = Flask(__name__)
websocket = GeventWebSocket()
from app import views
websocket.init_app(app)