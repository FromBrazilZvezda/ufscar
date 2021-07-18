from time import gmtime, sleep
import tweepy as tw
from os import environ

## config_time ##
post_hour = 17
post_minute = 30

## Tweepy_config ##
api_key = environ['api_key']
api_secret_key = environ['api_secret_key']
acess_key = environ['acess_key']
acess_secret = environ['acess_secret']
auth = tw.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(acess_key, acess_secret)
api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

while True:
    ## date_config ##
    gm_date_get = gmtime()
    day = gm_date_get[2]
    month = gm_date_get[1]
    year = gm_date_get[0]
    hour = gm_date_get[3]
    minute = gm_date_get[4]

    date_confirmation = "{}/{}/{}".format(year, month, day)
    hour_confirmation = "{}:{}".format(hour, minute)

    ## text_config ##
    a = open('configs.txt', 'r')
    sep = a.readlines()
    preliminar = []
    lista_final = []
    for item in sep:
        if item[0:10] == date_confirmation:
            preliminar.append(item)
    for item in preliminar:
        item1 = item[0:10]
        item2 = item[11:13]
        item3 = item[14:17]
        item4 = item[18:21]
        item5 = item[22:27]
        lista_final.append(item1)
        lista_final.append(item2)
        lista_final.append(item3)
        lista_final.append(item4)
        lista_final.append(item5)
    a.close()
    data = lista_final[0]
    ferias = int(lista_final[1])
    dias_aula = int(lista_final[2])
    total = int(lista_final[3])
    porcentagem = float(lista_final[4])


    if hour == int(post_hour) and minute == int(post_minute):
        if ferias > 0:
            post_frase = f'Ainda temos {ferias} de férias. O ENPE 2021/1 se inicia em 16 de Agosto de 2021.'
            api.update_status(post_frase)
            print('Atualizado.')
            sleep(60)

        elif ferias == 0 and dias_aula == 0:
                post_frase = f'As aulas começam amanhã! Boa sorte a todos <3'
                api.update_status(post_frase)
                print('Atualizado.')
                sleep(60)

        elif 0 < dias_aula > 103:
                post_frase = 'Já se passaram {} dias de aula no ENPE 2021/1. Completamos um total de {:.2f}% do semestre!'.format(dias_aula, porcentagem)
                api.update_status(post_frase)
                print('Atualizado.')
                print('{}'.format(date_confirmation))
                print('{}'.format(hour_confirmation))
                sleep(60)
                
        elif dias_aula == total:
                break

    else:
        print('Nada para atualizar.')
        print('{}'.format(date_confirmation))
        print('{}'.format(hour_confirmation))
        sleep(60)
        
## end_season_config ##
post_frase = '"Nós é merecedor de curti umas férias", RODO, Poze do. 2020.\nA partir de agora nós entraremos em stand-by para manutenção. Foi um prazer dividir esse semestre com vocês!'
api.update_status(post_frase)
print('Atualizado.')
