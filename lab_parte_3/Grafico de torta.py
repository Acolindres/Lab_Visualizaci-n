import pandas as pd
import plotly.graph_objects as go

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

# Crear el pie chart
fig = go.Figure(data=[go.Pie(labels=['Aprobados', 'No Aprobados'], values=[aprobados, no_aprobados])])

# Personalizar el diseño del gráfico
fig.update_layout(title='Distribución de aprobados',
                  showlegend=True)

# Mostrar el gráfico
fig.show()