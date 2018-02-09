#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '7LcRCDbolGOBGIuYbIv5ryUmI'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'QogLGe0hcbGXQ9qc0tgD4y7wegRSrLQyav6TsM9lj0ATESYbmy'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '962057914276966400-ADiPmZJ3AwyomBFhvhN76YncJTFSXJW'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'K86GE2iO4vtKK2Zc1QrmdwFvv50FTqC4PF3zYY9Bebo1M'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes
