import os
import sys


# get pdf file from user.
def get_pdf_file():
    while True:
        pdf_file = input(r'Enter pdf file path please:''\n')
        if not os.path.isfile(pdf_file):
            print('Wrong path/file please check and enter again')
        else:
            print('sounds good')
            break


get_pdf_file()
