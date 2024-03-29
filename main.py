import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/start.html')
        self.response.write(template.render())

class RunHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/run.html")
        self.response.write(template.render())

class JumpHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/jump.html")
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/run', RunHandler),
    ('/jump', JumpHandler),
], debug=True)
