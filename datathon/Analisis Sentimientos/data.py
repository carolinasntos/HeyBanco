import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('DataHey_cleaned.csv')

# Preprocesamiento de texto
# Aquí puedes realizar el preprocesamiento necesario, como eliminar caracteres especiales,
# convertir texto a minúsculas, eliminar stopwords, etc.

# Inicializar el analizador de sentimientos de NLTK
sid = SentimentIntensityAnalyzer()

# Aplicar el análisis de sentimientos al texto en la columna 'mensaje'
df['sentimiento'] = df['tweet'].apply(lambda mensaje: sid.polarity_scores(mensaje)['compound'])

# Determinar la polaridad dominante y escribir la polaridad que gana en una nueva columna
def determinar_polaridad_dominante(sentimiento):
    if sentimiento >= 0.05:
        return 'Positiva'
    elif sentimiento <= -0.05:
        return 'Negativa'
    else:
        return 'Neutral'

# Aplicar la función para determinar la polaridad dominante y escribir en una nueva columna
df['polaridad_dominante'] = df['sentimiento'].apply(determinar_polaridad_dominante)

# Calcular la polaridad que gana
polaridad_ganadora = df['polaridad_dominante'].value_counts().idxmax()

# Guardar el DataFrame con los resultados si es necesario
df.to_csv('/Users/carolinaresendz/Desktop/datathon/resultados.csv', index=False)