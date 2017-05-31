import bottle
import os
from api import names

app = application = bottle.default_app()

bottle.run(host="0.0.0.0")
