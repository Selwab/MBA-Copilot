import nltk
import os
from nltk.sentiment import SentimentIntensityAnalyzer


# Descarga el léxico de VADER
nltk.download('vader_lexicon')

# Descarga el tokenizador de oraciones Punkt
nltk.download('punkt')


def dividir_en_oraciones(texto):
    # Utiliza el tokenizador de oraciones Punkt para dividir el texto en oraciones
    oraciones = nltk.sent_tokenize(texto)
    return oraciones

def analizar_sentimiento(texto):
    # Obtiene las puntuaciones de sentimiento del texto
    puntuaciones = sia.polarity_scores(texto)

    # Clasifica el sentimiento del texto en función de las puntuaciones
    if puntuaciones['compound'] > 0.05:
        return 'positivo'
    elif puntuaciones['compound'] < -0.05:
        return 'negativo'
    else:
        return 'neutro'

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def analizar_casos_de_estudio(input_folder):
    files = os.listdir(input_folder)

    for file_name in files:
        input_file_path = os.path.join(input_folder, file_name)
        text_data = read_text_from_file(input_file_path)
        oraciones = dividir_en_oraciones(text_data)
        for i, oracion in enumerate(oraciones):
            sentimiento = analizar_sentimiento(oracion)
            print(f"Oración {i+1}: {oracion} Sentimiento: {sentimiento} ")

# Inicializa el analizador de sentimientos de VADER
sia = SentimentIntensityAnalyzer()

input_folder = 'StudyCases'
analizar_casos_de_estudio(input_folder)