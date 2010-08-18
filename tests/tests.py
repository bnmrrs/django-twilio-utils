import unittest
from django.http import HttpResponse, HttpRequest
from django_twilio_utils import decorators

@decorators.twilio_request(api_key='test', api_token='test')
def view_func(request):
	return HttpResponse(status=200)

class TwilioRequestDecoratorTest(unittest.TestCase):
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
		
if __name__ == '__main__':
	unittest.main()