import os


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


get_pdf_file()
