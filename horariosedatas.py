from datetime import date, time, datetime, timedelta

def tralhando_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/ %B /%Y'))

def trabalhando_time():
    horario = time(hour=19, minute=23, second=50)
    print(horario.strftime('%H:%M:%S'))

def trabalhando_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d:%m:%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    tupla = ('Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])

    data_criada = datetime(2017, 3, 18, 9, 45, 50)
    print(data_criada)

    data_string = '18/03/2017 09:45:55'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)

    nova_data = data_convertida -  timedelta(days=365, hours=3)
    print(nova_data)



if __name__ == '__main__':
    #tralhando_date()
     #trabalhando_time()
     trabalhando_datetime()