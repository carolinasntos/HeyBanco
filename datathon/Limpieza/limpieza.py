import pandas as pd

data = pd.read_csv('Datathon 2024 - Reto Hey - Dataset Público - Sheet1.csv')


data.info()

cols_use=['date', 'time']

#Eliminar las columnas
data= data.drop(columns=cols_use)

print(data)

#Eliminar filas repetidas
print(f'Tamaño del set antes de eliminar las filas repetidas: {data.shape}')
data.drop_duplicates(inplace=True)
print(f'Tamaño del set después de eliminar las filas repetidas: {data.shape}')

# Guardar el DataFrame en un archivo CSV
data.to_csv("/Users/carolinaresendz/Desktop/datathon/DataHey_cleaned.csv", index=False)