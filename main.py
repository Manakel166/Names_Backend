import bottle
from api import names

app = application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(host = '0.0.0.0')
