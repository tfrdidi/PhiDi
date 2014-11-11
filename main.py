#from flask import Flask
from phiDi import phidi
from phiDi import loadPage
import webapp2

#app = Flask(__name__)
#app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


class MainPage(webapp2.RequestHandler):

  def get(self):  # pylint:disable-msg=invalid-name
    """Handle GET requests."""
    self.response.header['Content-Type'] = "text/plain"
    self.response.out.write("Hello world")


class PhidiHandler(webapp2.RequestHandler):

    def get(self):
        q = self.request.get("q")
        self.response.out.write("your input was: " + q)


app = webapp2.WSGIApplication([('/.*', MainHandler), ('/phidi', PhidiHandler)], debug=True)

