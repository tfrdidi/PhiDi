from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/hidden')
def hidden():
    """Return a friendly HTTP greeting."""
    return 'Hidden functionality:'

@app.route('/greeting/<userName>')
def greeting(userName):
    """interpret input parameter."""
    return 'Hello: %s' % userName

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
