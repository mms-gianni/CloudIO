# Genereated and manually fixed 
# Gerator : https://github.com/demarey/cloudstack-client-generator
import hmac, hashlib
import base64
import os, sys
import urllib,urllib2
import json

class BaseCloudStackClient:
    def __init__(self, url, apiKey=None, secretKey=None):

        if (apiKey and secretKey):
            self.apiKey = apiKey
            self.secretKey = secretKey
            self.auth = True
        else:
            self.auth = False

        self.url=url

    def request(self, method, arguments):
        arguments['command'] = method
        arguments['response'] = 'json'

        if self.auth:
            arguments['apikey'] = self.apiKey

        params = []

        keys = sorted(arguments.keys())

        for k in keys:
            if arguments[k] != '':
                params.append(k + '=' + urllib.quote_plus(arguments[k]).replace("+","%20"))

        query = '&'.join(params)

        if self.auth:
            digest = base64.b64encode(
                hmac.new(
                    self.secretKey, 
                    msg=query.lower(), 
                    digestmod=hashlib.sha1
                ).digest()
            )
            
            query += '&signature=' + urllib.quote_plus(digest)
        #print "Request:", self.url+'?'+query
        try:
            response = urllib2.urlopen(self.url+'?'+query).read()
            mydict = json.loads(response)
            return mydict
        except Exception, e:
            print 'Error !', e
            sys.exit(2)
