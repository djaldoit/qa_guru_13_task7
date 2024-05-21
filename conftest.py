import shutil
import pytest
import zipfile
import os


tmp_dir = os.path.join(os.getcwd(), 'tmp')
zip_path = os.path.join(os.getcwd(), "zipped")
zip_resources = os.path.join(os.getcwd(), 'zipped', 'new_zip.zip')


@pytest.fixture(scope='function', autouse=True)
def zip_new_file():
    if not os.path.exists(zip_path):
        os.mkdir(zip_path)

    with zipfile.ZipFile(zip_path + '/new_zip.zip', 'w') as zip_file:
        for file in os.listdir(tmp_dir):
            add_file = os.path.join(tmp_dir, file)
            zip_file.write(add_file, os.path.basename(add_file))
            print(f'\nФайлы {file} - добавлен в архив')

    yield

    shutil.rmtree(zip_path)