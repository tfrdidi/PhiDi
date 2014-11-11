from phiDi import phidi
from phiDi import loadPage

import webapp2

querryName = "q"

class MainPage(webapp2.RequestHandler):

  def get(self): 
    self.response.headers["Content-Type"] = "text/html"
    self.response.out.write("""
        <form action="/phidi">
            <input type="text"name="q">
            <input type="submit">
        </form>
        """)


class PhidiHandler(webapp2.RequestHandler):

    def get(self):
        
        self.response.headers["Content-Type"] = "text/plain"
        
        articleName = self.request.get(querryName)
        # replace whitespaces to get a valid url
        articleName.replace(" ", "_")
        self.response.out.write('Distance of '+ articleName + ": " + str(phidi.getDistanceTo(articleName)))


app = webapp2.WSGIApplication([('/', MainPage), ('/phidi', PhidiHandler)], debug=True)

