import tweepy
from os import environ
from time import sleep, gmtime

# Time_config #
post_h = 22
post_m = 52

# Tweepy_config #
api_key = environ['api_key']
api_secret_key = environ['api_secret_key']
acess_key = environ['acess_key']
acess_secret = environ['acess_secret']
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(acess_key, acess_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# days_config #
vacation_days = 31
study_days = -31
total_study_days = 103

# math_config #
percentage = (study_days / total_study_days) * 100

# post_config #
while True:
    actual_time = gmtime()
    if actual_time[3] == int(post_h) and actual_time[4] == int(post_m):
        if vacation_days > 0:
            post_frase = f'Ainda temos {vacation_days} de férias. O ENPE 2021/1 se inicia em 16 de Agosto de 2021.'
            vacation_days = vacation_days - 1
            study_days = study_days + 1
            api.update_status(post_frase)
            print('Atualizado.')
            sleep(60)
            

        elif vacation_days == 0 and study_days == 0:
            post_frase = f'As aulas começam amanhã! Boa sorte a todos <3'
            study_days = study_days + 1
            api.update_status(post_frase)
            print('Atualizado.')
            sleep(60)
            
        elif 0 < study_days > 103:
            post_frase = 'Já se passaram {} dias de aula no ENPE 2021/1. Completamos um total de {:.2f}% do semestre!'.format(study_days, percentage)
            study_days = study_days + 1
            api.update_status(post_frase)
            print('Atualizado.')
            sleep(60)
            
        elif study_days == total_study_days:
            break
    else:
        print('Nada para atualizar.')
        sleep(60)
        
# end_season_config #
post_frase = '"Nós é merecedor de curti umas férias", RODO, Poze do. 2020.\nA partir de agora nós entraremos em stand-by para manutenção. Foi um prazer dividir esse semestre com vocês!'
api.update_status(post_frase)
print('Atualizado.')

 
