from flask import Flask
from flask_uwsgi_websocket import GeventWebSocket
app = Flask(__name__)
websocket = GeventWebSocket(app)
from app import views