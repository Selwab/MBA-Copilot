#Imports
import langchain 
import os 
from langchain.document_loaders import PyPDFLoader

# Crea la carpeta DataTxt donde estara los txt de cada pdf
def folderCreator  (output_folder):
    ruta_carpeta_cases = os.path.join(output_folder)

    if not os.path.exists(ruta_carpeta_cases):
        os.makedirs(ruta_carpeta_cases)
    
    return ruta_carpeta_cases

# funcion para cargar el pdf
def pdfLoader(path,pdfName):
    loader = PyPDFLoader(path+'/'+pdfName)
    return loader.load()

# Crea el txt para cada pdf
def creatorTxt (input_folder_PDF, output_folder) :

    cases = os.listdir(input_folder_PDF)
    pdfDocs_cases = []

    for case in cases:
        pdfDocs_cases.append(pdfLoader(input_folder_PDF,  case ))

    for i, doc_SC in enumerate(pdfDocs_cases):
        pdf_name = cases[i]

        # Elimina la extensión .pdf del nombre del archivo
        pdf_name = os.path.splitext(pdf_name)[0]

        doc_path = folderCreator (output_folder)

        text = ""
        
        # Itera a través de todas las páginas y acumular su contenido agregando un salto de linea
        for page in doc_SC:
            text += page.page_content + "\n" 

        # Guarda el texto acumulado en un solo archivo TXT para cada el PDF
        with open(os.path.join(doc_path, f"{pdf_name}.txt"), "w", encoding="utf-8") as file:
            file.write(text)
        
def extractorStudyCases (input_folder_PDF, output_folder):
    
    folderCreator (output_folder)
    creatorTxt (input_folder_PDF, output_folder)

    print("-------------------------------------------------------------------------------")
    print(f"You have extracted and converted your PDF files to txt inside: {output_folder}")
    print("-------------------------------------------------------------------------------")

"""
##### VARIABLES Y FUNCION PARA CORRER EL DATAEXTRACTOR #####
#current_directory = os.path.dirname(os.path.abspath(__file__))
input_folder_PDF = './Data/StudyCases/'
output_folder = 'StudyCases'

extractorStudyCases (input_folder_PDF, output_folder)
"""
