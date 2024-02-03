from ..LogicLayer.LevelGenerationLogic import LevelGenerationLogic
from flask import Flask

app = Flask(__name__)
config=""

@app.route('/generate_proper_level')
def generate_proper_level(email):
    return "Not Implemented"

