import matplotlib.pyplot as plt
import pandas as pd


hardware = pd.read_excel('hardware.xlsx', 'Sheet1')

fig = plt.figure()
hard = fig.add_subplot(2,1,1)
hard.plot(hardware['DIA_S'], hardware['HORAS'])

'''
soft = fig.add_subplot(2,1,2)
soft.plot()
'''

plt.show()
