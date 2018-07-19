import matplotlib.pyplot as plt

x = []
y = []

medir = open("numeros_lendo_e_plotando_2_exercicios.txt", "r")
for linha in medir:
    linha = linha.strip()
    POP, CIT = linha.split(";")
    x.append(POP)
    y.append(float(CIT))
medir.close()

#MANIPULAÇAO
figura = plt.figure()
background = figura.patch
background.set_facecolor("grey")

ax1 = figura.add_subplot(1,1,1)
ax1.plot(x, y, 'r', linestyle="-")
ax1.set_title("POPULACAO DE ALGUMAS CIDADES")
ax1.set_xlabel("NOMES CIDADES")
ax1.set_ylabel("POPULACAO (MIL) ")

plt.show()