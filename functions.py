import os
import PyPDF2
import shutil


# extract data from pdf file
def pdf_data_extract_extractor(pdf_file):
    with open(pdf_file, 'rb') as source_file:
        reader = PyPDF2.PdfFileReader(source_file)
        page = reader.getPage(0)
        text = page.extractText()
    return text


# transfer extracted data to destination file and turn to word
def transformer(saved_location, text_extracted, converted_name):
    extension_transform = converted_name.split('.')[0] + '.doc'
    multi_line_string = """""" + text_extracted
    with open(f"{saved_location}\\{extension_transform}", 'w') as writer:
        writer.writelines(multi_line_string)


# get path to save converted file
def get_destination_path_to_save():
    while True:
        path_to_save = input(r'please enter a path to save converted file:''\n')
        if not os.path.isdir(path_to_save):
            os.makedirs(f'{path_to_save}', exist_ok=False)
            break
        break

    return path_to_save


# get pdf file from user.
def get_pdf_file():
    while True:
        pdf_file = input(r'Enter pdf file path please:''\n')
        extract_file_name = pdf_file.split('\\')[-1]
        if not os.path.isfile(pdf_file) or extract_file_name.split('.')[-1] != 'pdf':
            print('Wrong path Or The file that has been entered is not pdf')
        else:
            break
    saved_files_location = get_destination_path_to_save()
    text_extracted = pdf_data_extract_extractor(pdf_file)
    transformer(saved_files_location, text_extracted, extract_file_name)


get_pdf_file()
