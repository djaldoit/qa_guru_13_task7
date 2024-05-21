import csv
import zipfile
import os
from pypdf import PdfReader
from openpyxl import load_workbook


zip_dir = os.path.join(os.getcwd(), 'tmp', 'new_zip.zip')
zip_path = os.path.join(os.getcwd(), 'tmp', 'new_zip.zip')


def test_pdf_file():
    with zipfile.ZipFile(zip_dir, 'r') as file_zip:
        with file_zip.open('file_pdf.pdf') as text_pdf:
            reader = PdfReader(text_pdf)
            text = reader.pages[0].extract_text()
            assert 'Y ou will need Adobe Acrobat Reader.' in text
            print('\nПроверка текста pdf-файла прошла успешно!')


def test_csv_file():
    with zipfile.ZipFile(zip_dir, 'r') as zip_file:
        with zip_file.open('file_csv.csv') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                print(row)


def test_xlsx_file():
    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        with zip_file.open('file_xlsx.xlsx') as file:
            workbook = load_workbook(filename=file)
            sheet = workbook.active
            print(sheet['A1'].value)
