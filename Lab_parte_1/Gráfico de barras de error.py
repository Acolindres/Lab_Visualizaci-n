import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

# Datos de errores para el gráfico de barras de error
errores_matematicas = rng.uniform(2, 5, 2)
errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

errores_ciencias = rng.uniform(1, 4, 2)
errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

errores_literatura = rng.uniform(3, 6, 2)
errores_literatura = [min(errores_literatura), max(errores_literatura)]

#usar np.mean de los errores de materias
errores_matematicas = np.mean(errores_matematicas)
errores_ciencias = np.mean(errores_ciencias)
errores_literatura = np.mean(errores_literatura)

# Calificaciones promedio en cada materia
promedio_matematicas = np.mean(matematicas)
promedio_ciencias = np.mean(ciencias)
promedio_literatura = np.mean(literatura)

# Gráfico de barras de error
materias = ['Matemáticas', 'Ciencias', 'Literatura']
promedios = [promedio_matematicas, promedio_ciencias, promedio_literatura]
errores = [errores_matematicas, errores_ciencias, errores_literatura]

plt.errorbar(materias, promedios , yerr= errores, fmt='o', capsize=5)
plt.title("Calificaciones promedio con errores en cada materia")
plt.xlabel('Materias')
plt.ylabel('Calificaciones promedio')
plt.show()