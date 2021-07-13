from os import environ
import tweepy
import time

## CONFIGURAÇÕES DO TWITTER ## 
api_key = environ['api_key']
api_secret_key = environ['api_secret_key']
acess_key = environ['acess_key']
acess_secret = environ['acess_secret']
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(acess_key, acess_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

## CONFIGURAÇÕES DE DIA ENPE ##
days = 138 
total_days = 138

# CONFIGURAÇÕES DE HORARIO DE POST ##
hour = 21
minute = 30

## CONFIGURAÇÕES NÃO ALTERÁVEIS ##
days_remaining = -(days - total_days)
perc = ((days - total_days) / total_days) * 100

## CONFIGURAÇÕES DE POST ##
while True:
    x = time.gmtime()
    if x[3] == int(hour) and x[4] == int(minute):
        post_frase =  f'Faltam {days} dias para o final do ENPE 2021/2 na @UFSCaroficial.'
        api.update_status(post_frase)
        print('Atualizado.')
        days = days - 1
        time.sleep(60)
    else:
        time.sleep(60)
        print('Não há o que atualizar.')
