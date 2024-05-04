import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Descargar recursos adicionales de NLTK (si aún no lo has hecho)
nltk.download('punkt')
nltk.download('stopwords')

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('Datathon 2024 - Reto Hey - Dataset Público - Sheet1.csv')

# Unir todos los tweets en un solo texto
todos_los_tweets = ' '.join(df['tweet'])

# Tokenizar el texto en palabras
tokens = word_tokenize(todos_los_tweets)

# Convertir todas las palabras a minúsculas para evitar duplicados
tokens = [word.lower() for word in tokens]

# Filtrar palabras que no sean útiles, como stopwords y signos de puntuación
stop_words = set(stopwords.words('spanish'))  # Se puede ajustar el idioma según sea necesario
tokens_filtrados = [word for word in tokens if word.isalnum() and word not in stop_words]

# Contar la frecuencia de cada palabra
frecuencia_palabras = Counter(tokens_filtrados)

# Obtener las palabras más comunes (por ejemplo, las 10 palabras más comunes)
palabras_mas_comunes = frecuencia_palabras.most_common(1000)

# Crear un DataFrame con las palabras más comunes y sus frecuencias
df_palabras_comunes = pd.DataFrame(palabras_mas_comunes, columns=['Palabra', 'Frecuencia'])

# Guardar el DataFrame de palabras más comunes en un archivo CSV
df_palabras_comunes.to_csv('palabras_comunes.csv', index=False)

# Crear un diccionario para almacenar las palabras y los tweets en los que aparecen
palabras_y_tweets = {palabra: [] for palabra, _ in palabras_mas_comunes}

# Llenar el diccionario con los tweets que contienen cada palabra
for tweet in df['tweet']:
    palabras_tweet = word_tokenize(tweet.lower())
    palabras_tweet = [palabra for palabra in palabras_tweet if palabra.isalnum() and palabra not in stop_words]
    for palabra in palabras_mas_comunes:
        if palabra[0] in palabras_tweet:
            palabras_y_tweets[palabra[0]].append(tweet)

# Crear un DataFrame para almacenar las palabras y los tweets en los que aparecen
filas = []
for palabra, tweets in palabras_y_tweets.items():
    for tweet in tweets:
        filas.append({'Palabra': palabra, 'Tweet': tweet})

df_palabras_y_tweets = pd.DataFrame(filas)

# Guardar el DataFrame de palabras y tweets en un archivo CSV
df_palabras_y_tweets.to_csv('tweets_palabrasComunes.csv', index=False)
