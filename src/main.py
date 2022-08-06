# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PIL import Image  # Importando o módulo Pillow para abrir a imagem no script

import pytesseract  # Módulo para a utilização da tecnologia OCR


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    image = Image.open('image.png')
    image_text = pytesseract.image_to_string(image=image)

    print(image_text)


if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
