# Programa que verifica se a puc ta aberta

from datetime import datetime
horario_abertura = 7*60 + 30
horario_fechamento = 23*60 + 10

hora_atual = int(input('Hora: '))
minuto_atual = int(input('Minutos: '))
horario_atual = hora_atual*60 + minuto_atual

if horario_abertura <= horario_atual <= horario_fechamento:
    print("A faculdade está aberta!")
else:
    print('A faculdade está fechada!')

