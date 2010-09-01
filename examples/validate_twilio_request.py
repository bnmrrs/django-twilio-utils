# settings.py
TWILIO_ACCOUNT_SID = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
TWILIO_ACCOUNT_TOKEN = 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'

#views.py
from django_twilio_utils.decorators import twilio_request

@twilio_request
def twilio_callback(request):
	# view_code_here