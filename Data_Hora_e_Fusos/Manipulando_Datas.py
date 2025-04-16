import datetime as dt

data = dt.datetime(2024, 4, 16)
print(data)

#Adicionando uma semana a data

data = data + dt.timedelta(weeks = 1)
print(data)