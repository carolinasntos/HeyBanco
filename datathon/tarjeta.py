import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

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

# Crear una expresión regular para buscar la palabra "tarjeta" en diferentes formas
regex_tarjeta = re.compile(r'\b(tarjeta|tarjetas|TARJETA|TARJETAS|¡Tarjeta!|¡TARJETA!|tarjeta\s*\!\s*|TARJETA\s*\!\s*)\b')

# Filtrar los tweets que contienen la palabra "tarjeta"
tweets_con_tarjeta = [tweet for tweet in df['tweet'] if regex_tarjeta.search(tweet)]

# Crear un DataFrame con los tweets que contienen la palabra "tarjeta"
df_tweets_con_tarjeta = pd.DataFrame(tweets_con_tarjeta, columns=['Tweet'])

# Guardar el DataFrame de tweets con la palabra "tarjeta" en un archivo CSV
df_tweets_con_tarjeta.to_csv('tweets_con_tarjeta.csv', index=False)

