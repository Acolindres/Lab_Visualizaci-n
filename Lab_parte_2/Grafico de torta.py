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

# Contar la cantidad de aprobados y no aprobados
aprobados = df[df['aprobado'] == 'Sí'].shape[0]
no_aprobados = df[df['aprobado'] == 'No'].shape[0]

# Crear los datos para el pie chart
datos = [aprobados, no_aprobados]
etiquetas = ['Aprobados', 'No Aprobados']

# Graficar la distribución de aprobados con un pie chart
plt.pie(datos, labels=etiquetas, autopct='%1.1f%%', startangle=90)

# Estilizar el pie chart
plt.title('Distribución de estudiantes aprobados')

# Mostrar el pie chart
plt.show()