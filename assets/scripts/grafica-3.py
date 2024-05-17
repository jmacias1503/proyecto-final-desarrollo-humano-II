import matplotlib.pyplot as plt

x = ["Si","No"]
y = [13,8]
plt.bar(x, y, color=["green","red"])

plt.title("Gestionar emociones", fontweight="bold")
plt.xlabel("Respuestas")
plt.ylabel("Cantidad de personas")

# Mostrar el gráfico
plt.show()
