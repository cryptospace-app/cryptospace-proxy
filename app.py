from flask import Flask
import json
import requests

app = Flask(__name__)
    
@app.route('/', methods=['GET'])
def get_winner():
    
    arg1 = request.args.get('name', '')
    return str(arg1)

    response = requests.get('https://kahoot.it/rest/challenges/' + id + '/progress')
    challenge = json.loads(response.text)
    leaders = challenge['leaderboard']['leaders']
    if len(leaders) > 0:
        return '"' + leaders[0]['playerId'] + '"'
    else:
        abort(400)
