#!/usr/bin/env python
#
# Copyright 2017 Mannir eSystems Limited.
# Saturday July 15, 2017 8:45 PM LOS
# Developed By Muhammad Mannir Ahmad (manniru@gmail.com)
# Updated MannirBot Python for Apengine using API.AI
#

import cgi
import datetime
import webapp2
import json, os, sys, random, linecache

from google.appengine.ext import ndb
from google.appengine.api import users
import re
#import requests
#from twilio.rest import Client
import hashlib

from mannir import mannir


import logging
import urllib
import urllib2

from mannirpy import remita
import time
from collections import namedtuple
# [START urlfetch-imports]
from google.appengine.api import urlfetch

import os.path
import sys

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = 'token'

exam_key = ndb.Key('Exam', 'default_exam')

class Exam(ndb.Model):
    author = ndb.UserProperty()
    content = ndb.TextProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('<h1>The Cloud Server is Online</h1')


class Test3(webapp2.RequestHandler):

    def get(self):
        #print mannir.sendsms(self, '07012223327', 'This is test sample from Google Appengine Python')
        #self.post()
        phone = '07012223327';
        message = 'This is test sample from Google Appengine Python'

        account_sid = "sid"
        auth_token = "token"

        client = Client(account_sid, auth_token)

        message = client.api.account.messages.create(to="+234702223327",
                                                     from_="+14242851118",
                                                     body="Hello From Twilio using Google Appengine Python")


class UrlPostHandler(webapp2.RequestHandler):
    """ Demonstrates an HTTP POST form query using urlfetch"""

    form_fields = {
        'orderID': '8792',
    }


    def get(self):

        MERCHANTID = '2547916'
        SERVICETYPEID = '4430731'
        APIKEY = '1946'
        GATEWAYURL = 'http://www.remitademo.net/remita/ecomm/v2/init.reg'
        GATEWAYRRRPAYMENTURL = 'http://www.remitademo.net/remita/ecomm/finalize.reg'
        CHECKSTATUSURL = 'http://www.remitademo.net/remita/ecomm'
        # 'http://'.$_SERVER['HTTP_HOST'].dirname($_SERVER['PHP_SELF'])
        PATH = 'https://4e3419b8.ngrok.io'

        order_id = '8792'

        concatString = order_id + APIKEY +MERCHANTID

        m = hashlib.sha512()
        m.update(concatString)
        hash = m.hexdigest()


        # $url 	= CHECKSTATUSURL . '/' . $mert  . '/' . $orderId . '/' . $hash . '/' . 'orderstatus.reg';
        url = CHECKSTATUSURL + '/' + MERCHANTID + '/' + order_id + '/' + hash + '/' + 'orderstatus.reg'

        try:
            result = urllib2.urlopen(url)
            self.response.headers['Content-Type'] = 'application/json'
            self.response.write(result.read())
        except urllib2.URLError:
            logging.exception('Caught exception fetching url')


        # try:
        #     form_data = urllib.urlencode(UrlPostHandler.form_fields)
        #     headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        #     result = urlfetch.fetch(
        #         url = url,
        #         payload=form_data,
        #         method=urlfetch.POST,
        #         headers=headers)
        #     self.response.write(result.content)
        # except urlfetch.Error:
        #     logging.exception('Caught exception fetching url')


        #self.response.out.write(url)


class MyDD2017(webapp2.RequestHandler):

    def get(self):
        ret = ''

        self.response.headers['Content-Type'] = 'application/json'

        self.response.out.write(json.dumps(ret))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/mydd2017', MyDD2017)
], debug=True)
