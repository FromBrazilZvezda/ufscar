## BOT QUE DIRÁ QUANTOS DIAS FALTAM PARA AS AULAS DA UFSCAR ACABERAM ##

from os import read, write
import tweepy
import time

api_key = 'XllhZnIxaVySKWfroSgWI1TXD'
api_secret_key = 'YT2NModGsIbqQyU36jVl59f1MAmd36QOE7bWsj6BnJ4kRIq86N'
acess_key = '1404917255100637195-dAu7bAf4Y39lpTOJ5CUvELSVaw8UJ7'
acess_secret = 'vAhi77ZW4E4jBdO8CGyUmmzbFm0TLPtoHO5GQgv0asFwx'
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(acess_key, acess_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

doc_name = 'days.txt'
total_days = 103


def get_days(doc_name):
    archive = open(doc_name, 'r+')
    days = int(archive.read())
    days_remaining = -(days - total_days)
    archive.close()
    return days_remaining


def get_percentage(doc_name):
    archive = open(doc_name, 'r+')
    days = int(archive.read())
    perc = (days / total_days) * 100
    archive.close()
    return '{:.2f}'.format(perc) 


def main(doc_name):
    while True:
        x = time.gmtime()
        if x[3] == 21 and x[4] == 30:
            days = get_days(doc_name)
            perc = get_percentage(doc_name)
            post_frase =  f'Faltam {days} dias para o final do ENPE 2021/1 na @UFSCar. Até o momento {perc}% do semestre ja foi concluído.'
            api.update_status(post_frase)
            archive = open(doc_name, 'r')
            actual_days = int(archive.read())
            archive.close()
            archive_2 = open(doc_name, 'w')
            new_day_qntt = actual_days + 1
            archive_2.write(str(new_day_qntt))
            archive_2.close()
            time.sleep(60)
        else:
            time.sleep(60)
    

main(doc_name)