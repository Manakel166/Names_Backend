import bottle
import os
from api import names

app = application = bottle.default_app()

if os.environ.get('APP_LOCATION') == 'heroku':
    bottle.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    bottle.run(host='localhost', port=8080, debug=True)
