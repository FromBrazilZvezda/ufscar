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

## CONFIGURAÇÕES FIXAS ##
post_hour = 23
post_minute = 30
tittle = 'days.txt'

## CONFIGURAÇÕES DE FUNÇÕES ##
def read_vac(tittle):
    archive = open(tittle, 'r')
    separation = []
    for item in archive.readlines():
        separation.append(item)
    archive.close()
    vac = int(separation[0][33:35])
    return vac


def read_days(tittle):
    archive = open(tittle, 'r')
    separation = []
    for item in archive.readlines():
        separation.append(item)
    archive.close()
    days = int(separation[1][13:16])
    return days


def read_total_days(tittle):
    archive = open(tittle, 'r')
    separation = []
    for item in archive.readlines():
        separation.append(item)
    archive.close()
    total_days = int(separation[1][22:25])
    return total_days


def change_days(tittle):
    archive = open(tittle, 'r')
    separation = []
    for item in archive.readlines():
        separation.append(item)
    archive.close()
    archive_2 = open('days.txt', 'w')
    
    vac = int(separation[0][33:35])
    new_vacation_days = 'vaccation_total_days_remaining = {}\n'.format(vac - 1)
    separation[0] = new_vacation_days

    days = int(separation[1][13:16])
    new_days = 'total_days = {}\n'.format(days + 1)
    separation[1] = new_days
    
    for item in separation:
        archive_2.write(item)

    archive_2.close


def main():
    while True:
        x = time.gmtime()
        if x[3] == int(post_hour) and x[4] == int(post_minute):
            post_frase =  f'Ainda temos {read_vac(tittle)} de férias. O ENPE 2021/1 se inicia em 16 de Agosto de 2021.'
            api.update_status(post_frase)
            print('Atualizado.')
            change_days(tittle)
            time.sleep(60)
        else:
            print('Não há o que atualizar.')
            time.sleep(60)
            

if __name__ == '__main__':
    main()
