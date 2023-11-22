import tabula
import os
import pandas

current_directory = os.path.dirname(os.path.abspath(__file__))

# Load the PDF file
pdf_data = tabula.read_pdf("D:/UNIVERSIDAD/PROYECTO DE INGENIERÍA DE SOFTWARE/chatBot_v2/chatBot/Data/SolutionMatrices/1637132923.pdf", pages="1", encoding='utf-8')

print(pdf_data)

# Concatenate the list of DataFrames into a single DataFrame
combined_df = pandas.concat(pdf_data, ignore_index=True)
#print(combined_df)

# Save to a CSV file
combined_df.to_csv("output_pag1.csv", index=False, encoding='utf-8')

text_data = combined_df.to_string(index=False)

headers = combined_df.columns
print(headers)

txt_file_path = "output_pag1.txt"

with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
    # Iterate through each column and write header and content to the text file
    for header in headers:
        txt_file.write(f'{header}:\n')
        # Combine the column data into a string, skipping NaN values
        column_data = combined_df[header].fillna('').to_string(index=False)
        txt_file.write(column_data + '\n')


