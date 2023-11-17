import os
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from langchain.document_loaders import WebBaseLoader

def preprocess_text(text):

    text = text.lower()
     
    text = re.sub('[^A-Za-z0-9áéíóúÁÉÍÓÚñÑ\s]+', '', text) 
    text = re.sub('\s+', ' ', text).strip()
    tokens = nltk.word_tokenize(text)

    return tokens

def remove_stopwords(tokens):
    stop_words= set(stopwords.words('spanish'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens

def clean_text(text):
    tokens = preprocess_text(text)
    filtered_tokens = remove_stopwords(tokens)
    clean_text = ' '.join(filtered_tokens)
    return clean_text

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def write_text_to_file(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

# Ruta de tu archivo de texto
file_path = './archivo.txt'
text_data = read_text_from_file(file_path)
cleaned_data = clean_text(text_data)
print(cleaned_data)
write_text_to_file('./archivolimpio.txt',cleaned_data)


#https://medium.com/@pawan329/text-data-preprocessing-made-easy-steps-to-clean-text-data-using-python-81a138a0e0e3
"""# Iterate through each link
for i, url in enumerate(urls):
    # Load the web page
    loader = WebBaseLoader(url)
    docs = loader.load()

    # Clean the text
    cleaned_text = re.sub('<.*?>', '', docs[0].page_content)  # Remove HTML tags
    cleaned_text = re.sub('[^A-Za-z0-9áéíóúÁÉÍÓÚñÑ\s]+', '', cleaned_text)  # Remove non-alphanumeric characters except spaces and Spanish accents
    cleaned_text = re.sub('\s+', ' ', cleaned_text).strip()  # Replace multiple spaces with a single space

    # Count words
    word_count = len(cleaned_text.split())

    # Check if the file already exists to avoid repetition
    filename = f'informacion/sitioweb{i+1}.txt'
    if not os.path.exists(filename):
        # Save the content in a file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cleaned_text)

        print(f"El documento {i+1} tiene {word_count} palabras.")
        """