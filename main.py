import bottle
import os
from api import names

app = application = bottle.default_app()

bottle.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
