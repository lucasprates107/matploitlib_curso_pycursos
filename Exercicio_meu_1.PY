import matplotlib.pyplot as plt

x = []
y = []

grafico = open('Arquivo_exercicio_meu_1.txt', 'r')
for linha in grafico:
    linha = linha.strip()
    PAIS, POP = linha.split('|')
    x.append(PAIS)
    y.append(float(POP))
grafico.close()

fig = plt.figure()
background = fig.patch
background.set_facecolor('grey')

ax1 = fig.add_subplot(1,1,1)
ax1.plot(x, y, 'black', linestyle="--")
ax1.set_title("POPULACAO DE PAISES DO MUNDO")
ax1.set_xlabel("NOME DOS PAISES")
ax1.set_ylabel("NUMERO DA POPULACAO(MILHOES)")

plt.show()