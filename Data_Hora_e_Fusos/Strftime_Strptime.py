from datetime import datetime as dt

data_hora_atual = dt.now()
data_hora_str = "2025-4-16 10:20"

mascara_ptbr = "%d/%m/%Y %a" #aqui define-se o formato que será retornado a data
#Nota: %a retorna o dia da semana na data específica
mascara_US = '%Y-%m-%d %H:%M'

print(data_hora_atual.strftime(mascara_ptbr))

print(dt.strptime(data_hora_str, mascara_US))