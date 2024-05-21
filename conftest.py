import pytest
import zipfile
import os
import time


tmp_dir = os.path.join(os.getcwd(), 'tmp')
zip_path = os.path.join(tmp_dir, 'new_zip.zip')


@pytest.fixture(scope='module', autouse=True)
def zip_new_file():
    zip_file = zipfile.ZipFile(zip_path, 'w')
    zip_file.write("tmp/file_csv.csv", arcname='file_csv.csv', compress_type=zipfile.ZIP_DEFLATED)
    zip_file.write("tmp/file_xlsx.xlsx", arcname='file_xlsx.xlsx', compress_type=zipfile.ZIP_DEFLATED)
    zip_file.write("tmp/file_pdf.pdf", arcname='file_pdf.pdf', compress_type=zipfile.ZIP_DEFLATED)
    zip_file.close()

    print(f'\nФайлы в zip: {zip_file.namelist()}')

    yield
    time.sleep(2)
    os.remove("tmp/new_zip.zip")
    print('\nФайл zip удален')
