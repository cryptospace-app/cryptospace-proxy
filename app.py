from flask import Flask
from flask import request
import json
import requests

app = Flask(__name__)
    
@app.route('/')
def get_winner():
    argNamesRaw = str(request.args.get('names')).split(';')
    argNames = [name.lower() for name in argNamesRaw]
    id = request.args.get('id')
    response = requests.get('https://kahoot.it/rest/challenges/' + id + '/progress')
    challenge = json.loads(response.text)
    players = challenge['leaderboard']['players']
    playerNames = []
    hasUnfinished = False
    hasMultipleGamesPlayed = False
    for player in players:
    	playerNames.append(player['playerId'].lower())
    	hasUnfinished |= player['gameUnfinished']
    	hasMultipleGamesPlayed |= (player['gamesPlayed'] > 1)
    playerNamesSet = set(playerNames)
    argNamesSet = set(argNames)
    if hasMultipleGamesPlayed or (len(playerNamesSet.difference(argNames)) > 0):
    	return ""
    if hasUnfinished or (len(argNamesSet) != len(playerNamesSet)):
    	abort(400)

    leaders = challenge['leaderboard']['leaders']
    if len(leaders) > 0:
        return '"' + leaders[0]['playerId'] + '"'
    else:
        abort(400)
