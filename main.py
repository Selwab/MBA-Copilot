import DataExtraction
import Cleansing
import Sentiment_Analyzer
import Splitting

def main ():
    ##### DATOS EXTRACTOR #####
    input_folder_PDF = './Data/StudyCases/'
    output_folder_TXT = 'StudyCases'

    DataExtraction.extractorStudyCases (input_folder_PDF, output_folder_TXT)

    ##### CLEANSING #####
    input_folder = 'StudyCases'
    output_folder = 'CleanStudyCases'
    Cleansing.process_files(input_folder, output_folder)
    
    print("-------------------------------------------------------------------------------")

    ##### SPLITTING #####

    # Configuración
    input_folder_clean = 'CleanStudyCases' 
    output_folder_splitting = 'ProcessedStudyCases'  
    chunk_size = 1800  
    overlap = 100       

    # Llamada a la función principal
    Splitting.process_and_split_files(input_folder_clean, output_folder_splitting, chunk_size, overlap)

    print("-------------------------------------------------------------------------------")

    ##### SENTIMENT ANALYZER #####

    Sentiment_Analyzer.analizar_casos_de_estudio(input_folder)

    print("-------------------------------------------------------------------------------")



if __name__ == '__main__':
    main()