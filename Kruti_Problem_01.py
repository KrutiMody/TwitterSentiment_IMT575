import oauth2 as oauth
import urllib.request as urllib
import json
'''
Aim here is simple, fetch tweets.
'''
'''
These are API Key, API Secret, Access Token Key and Access Token Secret which we get from Twitter Developer tool
We use these to authenticate ourselves and secure a connection with Twitter API
'''

api_key = "Bgr6Ysq7ZBIxhsewSRMFD6r30"
api_secret = "k2vIcQrL0oklLUyyJ5iZtQIMbUDLp6ZUwV991tG8M04HMPi3Gm"
access_token_key = "1079064211-kSpBzFIVjqSQYGgyYP4hsGejcHUncP64OvDEKzh"
access_token_secret = "938l5yxIDoDvnGujMmnlfxIuTH09CLvD7uqh02iUVmSGV"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = "https://stream.twitter.com/1.1/statuses/sample.json"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  lineValue = 0
  '''
  Here, our output file is 'write_attempt.txt'.
  We open the empty file and write each line from response with utf-8 encoding.
  Currently it is neither a json format nor a python dictionary, it is just a string and written down to our file.
  In next problem we will process each line by loading it as json and pick the tweet text
  '''
  with open('write_attempt.txt', 'w',encoding='utf-8') as f:
    for line in response:
    #lineValue += 1
    #if (lineValue < 21):
      #print(line.strip())
    #if line != "":
    #if dictionary.check(line):
      #tweet = json.loads(line)
      tweet = line.decode('utf-8').strip()
      print(tweet)
      f.write(str(tweet))
      f.write('\n')
    f.close()

if __name__ == '__main__':
  fetchsamples()

