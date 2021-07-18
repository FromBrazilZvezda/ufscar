from os import environ
from time import sleep, gmtime
import tweepy as tw

# CONFIGURAÇÃO DE HORÁRIO #
hr_postar = 21
min_postar = 30

# CONFIGURAÇÃO TWEEPY #
api_key = environ['api_key']
api_secret_key = environ['api_secret_key']
acess_key = environ['acess_key']
acess_secret = environ['acess_secret']
auth = tw.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(acess_key, acess_secret)
api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

while True:
    get_data = gmtime()
    dia = get_data[2]
    mes = get_data[1]
    ano = get_data[0]
    hora = get_data[3]
    minuto = get_data[4]

    data_auto = f'{dia}/{mes}/{ano}'

    lista_final = []

    if len(data_auto) == 8:
        a = open('configs.txt', 'r')
        lista_total = a.readlines()
        dados_dia_atual = []

        for item in lista_total:
            if item[0:8] == data_auto:
                dados_dia_atual.append(item)
        a.close()

        for item in dados_dia_atual:
            data = item[0:8]
            ferias = int(item[9:11])
            dias_aula = int(item[12:15])
            total = int(item[16:19])
            porcentagem = float(item[20:25])
            lista_final.append(data)
            lista_final.append(ferias)
            lista_final.append(dias_aula)
            lista_final.append(total)
            lista_final.append(porcentagem)
                    
    elif len(data_auto) == 9:
        a = open('configs.txt', 'r')
        lista_total = a.readlines()
        dados_dia_atual = []

        for item in lista_total:
            if item[0:9] == data_auto:
                dados_dia_atual.append(item)
        a.close()

        for item in dados_dia_atual:
            data = item[0:9]
            ferias = int(item[10:12])
            dias_aula = int(item[13:17])
            total = int(item[17:21])
            porcentagem = float(item[21:27])
            lista_final.append(data)
            lista_final.append(ferias)
            lista_final.append(dias_aula)
            lista_final.append(total)
            lista_final.append(porcentagem)

    elif len(data_auto) == 10:
        a = open('configs.txt', 'r')
        lista_total = a.readlines()
        dados_dia_atual = []

        for item in lista_total:
            if item[0:10] == data_auto:
                dados_dia_atual.append(item)
        a.close()

        for item in dados_dia_atual:
            data = item[0:10]
            ferias = int(item[12:14])
            dias_aula = int(item[14:18])
            total = int(item[18:22])
            porcentagem = float(item[22:27])
            lista_final.append(data)
            lista_final.append(ferias)
            lista_final.append(dias_aula)
            lista_final.append(total)
            lista_final.append(porcentagem)
    
    data_atual = lista_final[0]
    ferias = lista_final[1]
    dias_aula = lista_final[2]
    total = lista_final[3]
    porcentagem = lista_final[4]
   
    if hora == hr_postar and minuto == min_postar:
        if ferias > 0: 
            frase = f'Ainda temos {ferias} dias de férias. O ENPE 2021/1 se inicia em 16 de Agosto de 2021.'
            # api.update_status(frase)
            print(frase)
            print('Atualizado em {}.'.format(data_atual))
            sleep(60)

        elif ferias == 0 and dias_aula == 0:
            frase = f'As aulas do ENPE 2021/1 começam amanhã! tenham todos um ótimo semestre!'
            # api.update_status(frase)
            print(frase)
            print('Atualizado em {}'.format(data_atual))
            sleep(60)
        
        elif dias_aula > 0:
            frase = f'Já completamos {dias_aula} dias de aula no ENPE 2021/1, completando {porcentagem}% do total.'
            # api.update_status(frase)
            print(frase)
            print('Atualizado em {}'.format(data_atual))
            sleep(60)
        
        elif dias_aula == total:
            frase = f'O ENPE 2021/1 está 100% completo.'
            # api.update_status(frase)
            print(frase)
            print('Atualizado em {}'.format(frase))
            exit()
    else:
        print('Nada a atualizar.')
        print('Data: {}'.format(data_atual))
        print('Hora: {}:{}'.format(hora-3, minuto))
        print()
        sleep(60)
