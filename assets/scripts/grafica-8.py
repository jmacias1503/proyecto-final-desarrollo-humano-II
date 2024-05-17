import matplotlib.pyplot as plt

x = ["Si","No"]
y = [15,6]
plt.bar(x, y, color=["green","red"])

plt.title("Inteligencia intrapersonal en la resolucion de problemas", fontweight="bold")
plt.xlabel("Respuestas")
plt.ylabel("Cantidad de personas")

# Mostrar el gráfico
plt.show()
