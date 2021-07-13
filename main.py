from os import environ
import tweepy
import time

api_key = 'bFHqN6CHQVroUdXaGIOBlXrM2'
api_secret_key = 'JBgogY8HLwhzuupEYsCbKA4mTMJaV87PWj0O3AG4daghUg9vi2'
acess_key = '1404917255100637195-tteBC18NdLSdL0m1h7qHEj8zXiv2Lg'
acess_secret = 'rqaK5LUhXyuAtzIIuhr4AfjRYI21qBGPXUy8S4MAnViat'
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(acess_key, acess_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

days = 138 
total_days = 138
days_remaining = -(days - total_days)
perc = ((days - total_days) / total_days) * 100

while True:
    x = time.gmtime()
    if x[3] == 21 and x[4] == 30:
        post_frase =  f'Faltam {days} dias para o final do ENPE 2021/2 na @UFSCaroficial.'
        api.update_status(post_frase)
        print('postado!')
        days = days - 1
        time.sleep(60)
    else:
        time.sleep(60)
