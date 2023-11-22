import os
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Función para leer el contenido de un archivo de texto
def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Función para escribir texto en un archivo
def write_text_to_file(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

# Función para dividir el texto en fragmentos
def split_text_into_chunks(text, chunk_size, overlap):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    return splitter.split_text(text)

# Función principal para procesar y dividir los archivos
def process_and_split_files(input_folder, output_folder, chunk_size, overlap):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, file_name)
        text_data = read_text_from_file(input_file_path)

        # Dividir el texto en fragmentos
        chunks = split_text_into_chunks(text_data, chunk_size, overlap)

        # Guardar cada fragmento en un archivo separado
        base_name, _ = os.path.splitext(file_name)
        for i, chunk in enumerate(chunks):
            output_file_name = f'{base_name}_part{i+1}.txt'
            output_file_path = os.path.join(output_folder, output_file_name)
            write_text_to_file(output_file_path, chunk)
            print(f'Fragmento guardado en: {output_file_path}')

"""
# Configuración
input_folder = 'CleanStudyCases' 
output_folder = 'ProcessedStudyCases'  
chunk_size = 1800  
overlap = 100       

# Llamada a la función principal
process_and_split_files(input_folder, output_folder, chunk_size, overlap)
"""