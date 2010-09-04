from django.test import TestCase
from django.http import HttpResponse, HttpRequest
from django_twilio_utils.decorators import twilio_request
from django_twilio_utils.http import TwilioResponse

@twilio_request(api_key='test', api_token='test')
def view_func(request):
	return HttpResponse(status=200)

class TwilioRequestDecoratorTest(TestCase):
	def test_valid(self):
		request = HttpRequest()
		request.method = 'POST'
		response = view_func(request)
		
		self.failUnlessEqual(response.status_code, 200)
		
		
	def test_invalid(self):
		request = HttpRequest()
		request.method = 'POST'
		response = view_func(request)
		
		self.failUnlessEqual(response.status_code, 400)
		
class TwilioResponseTest(TestCase):
	def test_basic_usage(self):
		# Very basic usage with no verbs
		r = TwilioResponse()
		self.failUnlessEqual(str(r), 
"""Content-Type: application/xml

<?xml version='1.0'?><Response></Response>""")

		# Basic normal usage.  Should just have a say verb
		r = TwilioResponse().say('hello')
		self.failUnlessEqual(str(r),
"""Content-Type: application/xml

<?xml version='1.0'?><Response><Say voice='woman' loop='0' language='en'>hello</Say></Response>""")

		# Slightly more advanced usage.  Uses method chaining and all
		# currently implemented methods
		r = TwilioResponse().play(
			'hello.mp3'
		).record(
			'http://example.org/recording_callback'
		).gather(
			'http://example.org/gather_callback'
		).hangup()
		self.failUnlessEqual(str(r),
"""Content-Type: application/xml

<?xml version='1.0'?><Response><Play loop='0'>hello.mp3</Play><Record action='http://example.org/recording_callback' maxLength='60' finishOnKey='#' timeout='5' method='POST' playBeep='false' /><Gather action='http://example.org/gather_callback' numDigits='1' finishOnKey='#' timeout='5' method='POST' /><Hangup /></Response>""")

def test_nested(self):
	pass