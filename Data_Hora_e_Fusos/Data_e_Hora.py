from datetime import date, datetime

data = date(2023, 7, 10)
print(data)
print(date.today())

data_hora = datetime(2023, 7, 10, 12, 30, 45)
#Ao utilizar date time se escreve na ordem (YYYY/MM/AA - H/MIN/SEC) 
#Nota: Horário é opcional, mas data é obrigatório

print(data_hora)