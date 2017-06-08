from bottle import request, response
from bottle import post, get, put, delete
from bottle import view
from bottle import route, run
from bottle import hook

_names = set("Woody")                    # the set of names


import re, json

namepattern = re.compile(r'^[a-zA-Z\d]{1,64}$')


_allow_origin = '*'
_allow_methods = 'PUT, GET, POST, DELETE, OPTIONS'
_allow_headers = 'Authorization, Origin, Accept, Content-Type, X-Requested-With'

@hook('after_request')
def enable_cors():
    '''Add headers to enable CORS'''

    response.headers['Access-Control-Allow-Origin'] = _allow_origin
    response.headers['Access-Control-Allow-Methods'] = _allow_methods
    response.headers['Access-Control-Allow-Headers'] = _allow_headers

@route('/', method = 'OPTIONS')
@route('/<path:path>', method = 'OPTIONS')
def options_handler(path = None):
    return

@route('/')
@view('index')
def homepage():
    return dict()

@route('/listName')
@view('listName')
def listNames():
    return dict()


@route('/addNames', method="GET")
@view('addNames')
def addNames():
    return dict()

@route('/modifyName')
@view('modifyName')
def modifyNames():
    return dict()

@route('/deleteName')
@view('deleteName')
def deleteNames():
    return dict()


@get('/names')
def listing_handler():
    '''Handles name listing'''

    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return json.dumps({'names': list(_names)})

@post('/names')
def creation_handler():
    '''Handles name creation'''

    try:
        # parse input data
        try:
            data = request.json
        except:
            raise KeyError

        if data is None:
            raise ValueError

        # extract and validate name
        try:
            if namepattern.match(data['name']) is None:
                raise ValueError
            name = data['name']
        except (TypeError, KeyError):
            raise ValueError

        # check for existence
        if name in _names:
            raise KeyError

    except ValueError:
        # if bad request data, return 400 Bad Request
        response.status = 400
        return

    except KeyError:
        # if name already exists, return 409 Conflict
        response.status = 409
        return

    # add name
    _names.add(name)

    # return 200 Success
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return json.dumps({'name': name})

@put('/names/<oldname>')
def update_handler(oldname):
    '''Handles name updates'''

    try:
        # parse input data
        try:
            data = request.json
            print(data)
        except:
            raise ValueError

        newname = data["newname"]
        print(oldname)
        print(newname)

        # extract and validate new name
        try:
            if namepattern.match(oldname) is None:
                raise ValueError
            if namepattern.match(newname) is None:
                raise ValueError
        except (TypeError, KeyError):
            raise ValueError

        # check if updated name exists
        if oldname not in _names:
            raise ValueError

        # check if new name exists
        if newname in _names:
            raise KeyError(409)

    except ValueError:
        response.status = 400
        return "No name matched"
    except KeyError as e:
        response.status = e.args[0]
        return "this name is already in database"

    # add new name and remove old name
    _names.remove(oldname)
    _names.add(newname)

    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return json.dumps({'name': newname})

@delete('/names/<name>')
def delete_handler(name):
    '''Handles name updates'''

    try:
        # parse input data
        if name is None:
            raise ValueError

        # check for existence
        if name not  in _names:
            raise KeyError


    except ValueError:
        # if bad request data, return 400 Bad Request
        print("error value")
        response.status = 400
        return
    except KeyError:
        # if name already exists, return 409 Conflict
        print("error status")
        response.status = 404
        return

    _names.remove(name)

    # Remove name

    return {}

@get('/INIT')
def init_database():
    _names.clear()
    _names.add("Woody")
    response.status = 200
    return
    

