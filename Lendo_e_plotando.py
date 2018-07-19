import matplotlib.pyplot as plt

x = []
y = []

valor = open("numeros_lendo_plotando.csv", "r")
for numero in valor:
    numero = numero.strip()
    X, Y = numero.split(",")
    x.append(X)
    y.append(Y)
valor.close()

plt.plot(x, y)
plt.title("TITULO DO GRAFICO")
plt.xlabel("TITULO EIXO X")
plt.ylabel("TITULO EIXO Y")
plt.show()