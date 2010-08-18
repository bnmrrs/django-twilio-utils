#
#  The MIT License
#
#  Copyright (c) 2010 Ben Morris
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.



try:
	from functools import wraps
except ImportError:
	from django.utils.functional import wraps
	
from twiliosimple import Utils
	
from django.http import HttpResponse
from django.conf import settings
from django.utils.decorators import available_attrs

def twilio_request(function=None, api_key=None, api_token=None):
	if api_key is None:
		api_key = settings.TWILIO_API_SID
	if api_token is None:
		api_token = settings.TWILIO_API_TOKEN
		
	def decorator(view_func):
		def _wrapped_view(request, *args, **kwargs):
			if is_valid_twilio_request(request, api_key, api_token):
				return view_func(request, *args, **kwargs)
			return HttpResponse(status=400)
		return wraps(view_func, assigned=available_attrs(view_func))(_wrapped_view)

	if function is None:
		return decorator
	else:
		return decorator(function)
		

def is_valid_twilio_request(request, api_key, api_token):
	if not request.method == 'POST':
		return False
		
	try:
		signature = request.META['HTTP_X_TWILIO_SIGNATURE']
	except KeyError:
		return False

	twilio_utils = Utils(api_key, api_token)
	current_url = request.build_absolute_uri()

	return twilio_utils.validateRequest(current_url, request.POST, signature)