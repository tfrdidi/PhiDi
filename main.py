from phiDi import phidi
from phiDi import loadPage

import webapp2


class MainPage(webapp2.RequestHandler):

  def get(self): 
    return loadPage.showPhilosophersPage()


class PhidiHandler(webapp2.RequestHandler):

    def get(self):
        q = self.request.get("q")
        self.response.out.write("your input was: " + q)


app = webapp2.WSGIApplication([('/.*', MainPage), ('/phidi', PhidiHandler)], debug=True)

