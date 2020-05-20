from flask import Flask
from flask import request
import json
import requests

app = Flask(__name__)
    
@app.route('/')
def get_winner():
    names = request.args.get('names')
    id = request.args.get('id')
    response = requests.get('https://kahoot.it/rest/challenges/' + id + '/progress')
    challenge = json.loads(response.text)
    leaders = challenge['leaderboard']['leaders']
    if len(leaders) > 0:
        return '"' + leaders[0]['playerId'] + '"'
    else:
        abort(400)
