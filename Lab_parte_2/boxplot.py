import pandas as pd
import matplotlib.pyplot as plt

# Crear el DataFrame con los datos del dataset
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'],
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

filas_materias = df[df['materia'].isin(['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'])]

# Graficar la distribución de notas con un boxplot
plt.boxplot([filas_materias[filas_materias['materia'] == 'Matemáticas']['nota'], filas_materias[filas_materias['materia'] == 'Historia']['nota'], filas_materias[filas_materias['materia'] == 'Ciencias']['nota'], filas_materias[filas_materias['materia'] == 'Lenguaje']['nota']])

plt.xticks([1, 2, 3, 4], ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'])
# Estilizar el boxplot
plt.title('Distribución de notas')
plt.xlabel('Notas')
plt.ylabel('Nota')

# Mostrar el boxplot
plt.show()