from phiDi import phidi
from phiDi import loadPage

import webapp2

import os.path


class MainPage(webapp2.RequestHandler):

  def get(self):  # pylint:disable-msg=invalid-name
    return open(os.path.dirname(__file__) + "/pages/philosophers.html")


class PhidiHandler(webapp2.RequestHandler):

    def get(self):
        q = self.request.get("q")
        self.response.out.write("your input was: " + q)


app = webapp2.WSGIApplication([('/.*', MainPage), ('/phidi', PhidiHandler)], debug=True)

