import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2,3,6,8,2]
plt.bar(x, y)

plt.title("Capacidad de conocerte", fontweight="bold")
plt.xlabel("Capacidad")
plt.ylabel("Cantidad de personas")

# Mostrar el gráfico
plt.show()
