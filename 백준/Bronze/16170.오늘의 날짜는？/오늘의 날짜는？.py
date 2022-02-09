from datetime import datetime
x = datetime.utcnow()
print(x.year, '%02d'% x.month, '%02d'% x.day, sep='\n')