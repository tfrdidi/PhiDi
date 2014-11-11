#from flask import Flask
from phiDi import phidi
from phiDi import loadPage
import webapp2

#app = Flask(__name__)
#app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


class MainHandler(webapp2.RequestHandler):

  def get(self):  # pylint:disable-msg=invalid-name
    """Handle GET requests."""
    self.response.header['Content-Type'] = "text/plain"
    self.response.out.write("Hello world")


APP = webapp2.WSGIApplication([('/.*', MainHandler),], debug=True)

