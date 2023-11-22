#Imports
import langchain 
import os 
import openai
from langchain.document_loaders import PyPDFLoader
import pandas as pd

# Crea la carpeta DataTxt donde estara los txt de cada pdf
def folderCreator  (currDirectory, outputFolder):
    ruta_carpeta_cases = os.path.join(currDirectory, outputFolder)

    if not os.path.exists(ruta_carpeta_cases):
        os.makedirs(ruta_carpeta_cases)
    
    return ruta_carpeta_cases

# funcion para cargar el pdf
def pdfLoader(path,pdfName):
    loader = PyPDFLoader(path+'/'+pdfName)
    return loader.load()

# Crea el txt para cada pdf
def creatorTxt (currDirectory, subDirectory, outputDirectory) :

    cases = os.listdir(currDirectory + subDirectory)
    pdfDocs_cases = []

    for case in cases:
        pdfDocs_cases.append(pdfLoader(currDirectory + subDirectory,  case ))

    for i, doc_SC in enumerate(pdfDocs_cases):
        pdf_name = cases[i]

        # Elimina la extensión .pdf del nombre del archivo
        pdf_name = os.path.splitext(pdf_name)[0]

        doc_path = folderCreator (currDirectory, outputDirectory)

        text = ""
        
        # Itera a través de todas las páginas y acumular su contenido agregando un salto de linea
        for page in doc_SC:
            text += page.page_content + "\n" 

        # Guarda el texto acumulado en un solo archivo TXT para cada el PDF
        with open(os.path.join(doc_path, f"{pdf_name}.txt"), "w", encoding="utf-8") as file:
            file.write(text)
        
def extractorStudyCases (currDirectory, subDirectoryForLoad, output_Directory):
    
    folderCreator (currDirectory, output_Directory)
    creatorTxt (currDirectory, subDirectoryForLoad , output_Directory)

    print("------------------------------------------------------")
    print("You have extracted and converted your PDF files to txt")
    print("------------------------------------------------------")

# Función para procesar cada archivo CSV del folder y extraer secciones a archivos TXT
def process_csv_folder_to_txt(current_directory, csv_directory, output_txt_directory):
    csv_folder_path = current_directory + '\\' + csv_directory
    output_path = current_directory + '\\' + output_txt_directory

    csv_files = [file for file in os.listdir(csv_folder_path) if file.endswith('.csv')]
    
    for csv_file in csv_files:
        csv_path = csv_folder_path + '\\' + csv_file
        df = pd.read_csv(csv_path)
        
        csv_name = os.path.splitext(csv_file)[0]

        text = ""
        for column in df.columns:
            section_text = df[column].tolist()
            text += f"--- {column} ---\n"
            for item in section_text:
                if pd.notnull(item):
                    text += "%s\n" % item
            text += "\n\n"

        with open(output_path + '\\' + f"{csv_name}.txt", "w", encoding="utf-8") as file:
            file.write(text)


def extract_solution_matrices(current_directory, csv_directory, output_txt_directory):
    folderCreator (current_directory, output_txt_directory)
    process_csv_folder_to_txt(current_directory, csv_directory, output_txt_directory)
    print("------------------------------------------------------")
    print("You have extracted and converted your Matrix Solutions files to txt")
    print("------------------------------------------------------")

###
##### VARIABLES Y FUNCION PARA CORRER EL DATAEXTRACTOR #####
current_directory = os.path.dirname(os.path.abspath(__file__))
csv_directory = '/Data/SolutionMatrices'  # Directorio que contiene los archivos CSV
pdf_directory = '/Data/StudyCases'  # Directorio que contiene los archivos PDF
output_pdf_directory  = 'StudyCases'

extractorStudyCases (current_directory, pdf_directory, output_pdf_directory)

output_csv_directory = 'StudyCases'  # Directorio de salida para los archivos TXT

# Ejecutar el proceso principal
extract_solution_matrices(current_directory, csv_directory, output_csv_directory)