import pandas as pd
import plotly.graph_objects as go

data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'],
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)
filas_materias = df[df['materia'].isin(['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'])]

# Crear una lista de datos para cada materia
datos_materias = [
    filas_materias[filas_materias['materia'] == 'Matemáticas']['nota'],
    filas_materias[filas_materias['materia'] == 'Historia']['nota'],
    filas_materias[filas_materias['materia'] == 'Ciencias']['nota'],
    filas_materias[filas_materias['materia'] == 'Lenguaje']['nota']
]

# Crear la figura con el gráfico de caja
fig = go.Figure()
for i, materia in enumerate(['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje']):
    fig.add_trace(go.Box(y=datos_materias[i], name=materia))

# Personalizar el diseño del gráfico
fig.update_layout(title='Distribución de notas',
                  xaxis_title='Materia',
                  yaxis_title='Nota')

# Mostrar el gráfico
fig.show()