from flask import Flask

from router import init_routes

app = Flask(__name__)

init_routes(app)
