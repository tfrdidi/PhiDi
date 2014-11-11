from phiDi import phidi
from phiDi import loadPage

import webapp2


class MainPage(webapp2.RequestHandler):

  def get(self): 
    self.response.headers["Content-Type"] = "text/html"
    self.response.out.write("""
        <form action="/phidi">
            <input type="text"name="test">
            <input type="submit">
        </form>
        """)


class PhidiHandler(webapp2.RequestHandler):

    def get(self):
        q = self.request.get("q")
        self.response.out.write("your input was: " + q)


app = webapp2.WSGIApplication([('/.*', MainPage), ('/phidi', PhidiHandler)], debug=True)

