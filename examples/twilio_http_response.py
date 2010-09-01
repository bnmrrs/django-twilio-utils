# views.py
from django_twilio_utils.decorators import twilio_request
from django_twilio_utils.http import TwilioResponse

@twilio_request # Validate that the request did come from Twilio
def twilio_callback(request):
	# Have Twilio say "Thanks for calling!" and then end the call
	return TwilioResponse().say('Thanks for calling!').hangup()