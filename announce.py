#Result announce
#Author:V
#Language:Python/app-engine

import urllib2

from google.appengine.api import mail
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class homepage(webapp.RequestHandler):
	def get(self):
		u=urllib2.urlopen("http://uoc.ac.in/exam/btech/creditresnet188.php?id=2247&regno=etakech045&Submit=Submit")
		size=u.info().get('Content-Length')
		if size>1500:
			self.mail()
		self.response.out.write('done')

	def mail(self):
		to="gecgitrepository@gmail.com"
		sub="Results!!!!!!"
		announce_body='''Result vanne....:-)
		http://uoc.ac.in/exam/btech/creditresnet188.php?id=2247&regno=etakecs045&Submit=Submit'''
		mail.send_mail(sender='Result <rajeevs1992@gmail.com>',
						to=to,
						subject=sub,
						body=announce_body)

application=webapp.WSGIApplication([('/',homepage)],debug=True)
run_wsgi_app(application)
