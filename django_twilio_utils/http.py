from twiliosimple import Response
from django.http import HttpResponse

class TwilioResponse(Response, HttpResponse):
	def __init__(self):
		super(TwilioResponse, self).__init__(mimetype='application/xml')
		
	def __str__(self):
		"""Full HTTP message, including headers."""
		return '\n'.join(['%s: %s' % (key, value)
			for key, value in self._headers.values()]) \
			+ '\n\n' + self.getcontent()