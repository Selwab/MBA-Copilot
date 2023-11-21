#Imports
import langchain 
import os 
import openai
from langchain.document_loaders import PyPDFLoader

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

###
##### VARIABLES Y FUNCION PARA CORRER EL DATAEXTRACTOR #####
current_directory = os.path.dirname(os.path.abspath(__file__))
subDirectoryLoad = '/Data/StudyCases/'
DirectoryOutput = 'StudyCases'

extractorStudyCases (current_directory, subDirectoryLoad, DirectoryOutput)

