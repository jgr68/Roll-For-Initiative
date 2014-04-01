from flask import Flask

app = Flask(__name__)
app.debug = False
#app.config.from_object('config')

from app import views
