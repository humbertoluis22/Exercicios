from datetime import datetime

data = datetime.now()
print(type(data))
data_formatada = datetime.strftime(data,'%d/%B/%Y - %H:%M:%S')
print(data_formatada)