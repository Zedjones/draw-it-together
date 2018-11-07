from flask import Flask 

app = Flask(__name__)

from draw_it_together import routes
