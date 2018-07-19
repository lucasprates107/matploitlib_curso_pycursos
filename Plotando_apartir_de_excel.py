import matplotlib.pyplot as plt
import pandas as pd

ler = pd.read_excel('excel_grafic.xlsx', 'Sheet1')

plt.plot(ler['CIDADES'], ler['POP'])
plt.title('POPULACAO DE CITY')
plt.xlabel('CIDADES')
plt.ylabel('POPULACAO')
plt.show()