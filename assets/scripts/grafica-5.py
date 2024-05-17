import matplotlib.pyplot as plt

x = ["Si","No"]
y = [21,0]
plt.bar(x, y, color=["green","red"])

plt.title("Influecia del autoconocimiento en lo laboral", fontweight="bold")
plt.xlabel("Respuestas")
plt.ylabel("Cantidad de personas")

# Mostrar el gráfico
plt.show()
