from flask import Flask
import json
import requests
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
    
@app.route('/winner-of/<string:id>')
def get_winner(id):
    response = requests.get('https://kahoot.it/rest/challenges/' + id + '/progress')
    challenge = json.loads(response.text)
    leaders = challenge['leaderboard']['leaders']
    if len(leaders) > 0:
        return leaders[0]['playerId']
    else:
        abort(400)
