from flask import Flask
import json
import requests

app = Flask(__name__)
    
@app.route('/winner-of')
def get_winner():
    challengeId = request.args.get('id')
    response = requests.get('https://kahoot.it/rest/challenges/' + challengeId + '/progress')
    challenge = json.loads(response.text)
    leaders = challenge['leaderboard']['leaders']
    if len(leaders) > 0:
        return '"' + leaders[0]['playerId'] + '"'
    else:
        abort(400)
