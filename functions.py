import os
import sys


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
