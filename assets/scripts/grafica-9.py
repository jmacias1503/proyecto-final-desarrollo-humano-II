import matplotlib.pyplot as plt

x = ["Si","No"]
y = [17,4]
plt.bar(x, y, color=["green","red"])

plt.title("Deberia ser mas valorada la inteligencia intrapersonal", fontweight="bold")
plt.xlabel("Respuestas")
plt.ylabel("Cantidad de personas")

# Mostrar el gráfico
plt.show()
