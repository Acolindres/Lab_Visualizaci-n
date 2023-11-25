import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(42)


# Datos de calificaciones de los estudiantes

matematicas = rng.integers(50, 100, 20)

plt.hist(matematicas, bins=10, edgecolor="green", color= "red")
plt.title("Distribucion de las calificaciones de Matematicas.")
plt.xlabel('Calificaciones de Matematicas')
plt.ylabel('Frecuencias')
plt.show()