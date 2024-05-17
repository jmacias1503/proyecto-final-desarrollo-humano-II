import matplotlib.pyplot as plt

x = ["Si","No"]
y = [10,11]
plt.bar(x, y, color=["green","red"])

plt.title("Personas motivadas", fontweight="bold")
plt.xlabel("Respuestas")
plt.ylabel("Cantidad de personas")

# Mostrar el gráfico
plt.show()
