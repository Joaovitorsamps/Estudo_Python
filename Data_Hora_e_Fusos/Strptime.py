#Converte string para formato datetime

import datetime as dt

data = dt.datetime.now()

#Convertendo string para datetime
date_string = "20/07/2023 15:30"
data = dt.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(data)