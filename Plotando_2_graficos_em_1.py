import matplotlib.pyplot as plt

def ler_dados(montar):

        x = []
        y = []

        medir = open(montar, "r")
        for linha in medir:
            linha = linha.strip()
            POP, CIT = linha.split(";")
            x.append(POP)
            y.append(float(CIT))
        medir.close()
        return x, y

x, y = ler_dados('numeros_lendo_e_plotando_2_exercicios.txt')
x2, y2 = ler_dados('numeros_lendo_plotando.csv')

figura = plt.figure()
background = figura.patch
background.set_facecolor("grey")

ax1 = figura.add_subplot(1,1,1)
ax1.plot(x, y, 'r', linestyle="-", label='grafico1')
ax1.plot(x2, y2, 'b', linestyle="--", label='grafico2')
ax1.legend(loc='upper right')

ax1.set_title("POPULACAO DE ALGUMAS CIDADES")
ax1.set_xlabel("NOMES CIDADES")
ax1.set_ylabel("POPULACAO (MIL) ")

plt.show()