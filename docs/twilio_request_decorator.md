# twilio_request

## Overview
twilio_request is a decorator for validating Twilio callback requests.  It takes your API key and API token and validates that the request did indeed come from Twilio.  If not it returns a 400 HTTP status.

## Usage

### Manually adding the api_key and api_token
For the basic usage you need to provide twilio\_request with your api\_key and api\_token
<pre><code>from django_twilio_utils.decorators import twilio_request

@twilio_request(api_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', api_token='yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
def twilio_callback(request):
    # view_code_here</code></pre>

### Providing the api_key and api_token in settings.py
If you don't want to provide your api\_key and api\_token with every view using this decorator you can specify it in settings.py as follows

<pre><code># settings.py

TWILIO_ACCOUNT_SID = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
TWILIO_ACCOUNT_TOKEN = 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'</code></pre>

and then leave it out of your decorator in views.py

<pre><code># views.py

from django_twilio_utils.decorators import twilio_request

@twilio_request
def twilio_callback(request):
	# view_code_here</code></pre>