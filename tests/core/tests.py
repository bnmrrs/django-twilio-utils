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
		r = TwilioResponse()

		self.failUnlessEqual(str(r), 
"""Content-Type: application/xml

<?xml version='1.0'?><Response></Response>""")

def test_complex(self):
	pass