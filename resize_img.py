import os
import subprocess

directory = 'Source'
current_dir = os.path.dirname(os.path.abspath(__file__))
path_to_directory = os.path.join(current_dir, directory)
px = str(200)

def convert_img(path, px):
    list_of_img = os.listdir(path=path)
    for img in list_of_img:
        subprocess.run(['convert', os.path.join(path, img), '-resize', px , os.path.join(path, 'resize'+img)])
        print('{} обработан!'.format(img))

if __name__ == '__main__':

    convert_img(path_to_directory, px)

    pass
