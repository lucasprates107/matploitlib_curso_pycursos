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

plt.plot(x, y)
plt.title("POPULACAO DE ALGUMAS CIDADES")
plt.xlabel("NOMES CIDADES")
plt.ylabel("POPULACAO (MIL) ")
plt.show()