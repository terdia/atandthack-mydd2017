# Bismillahir Rahamanir Rahim
# Developed By: Muhammad Mannir AHmad
# Tuesday 18, July, 2017 4:00 PM LOS
import urllib2

import logging
import urllib

# [START urllib2-imports]
import urllib2
# [END urllib2-imports]

# [START urlfetch-imports]
from google.appengine.api import urlfetch

class mannir:

    def sendsms1(phone, message):
        print 1
        url = 'http://www.smslive247.com/http/index.aspx'
        payload = {
            'cmd': 'sendquickmsg',
            'owneremail': 'manniru@gmail.com',
            'subacct': 'MANNIR',
            'sender': 'MANNIR',
            'subacctpwd': 'muhammad',
            'sendto': phone,
            'message': message,
        }

        response = requests.post(url, data=payload)
        response.raise_for_status()
        return response.text

    def sendsms(self, message, phone):
        payload = {
            'cmd': 'sendquickmsg',
            'owneremail': 'manniru@gmail.com',
            'subacct': 'MANNIR',
            'sender': 'MANNIR',
            'subacctpwd': 'muhammad',
            'sendto': phone,
            'message': message,
        }

        try:
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            result = urlfetch.fetch(
                url='http://www.smslive247.com/http/index.aspx',
                payload=payload,
                method=urlfetch.POST,
                headers=headers)
            self.response.write(result.content)
            print result.content
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')
