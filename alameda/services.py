import pdf2image
import pytesseract as pyt
import json
import random


# convert pdf to images
def convert_to_image(path: str):
    print('Converting PDF to Images...')
    return pdf2image.convert_from_path(path)


# use tesseract for OCR
def get_data_as_dict(image):
    return pyt.image_to_data(image, output_type=pyt.Output.DICT)


# write in a demo file
def write_in_tmp(data_dict):
    file_name = 'tmp/{}'.format(random.random())
    with open(file_name, 'w') as file:
        file.write(json.dumps(data_dict))
    file.close()


# form data from arr
def form_data(arr):
    result = ''
    for i in arr:
        result += i + ' '

    return result.strip()


# form json key from simple words
def get_json_key(string):
    arr = string.split(' ')
    string = arr[0]
    arr = [i.lower() for i in arr]

    for i in range(1, len(arr)):
        arr[i] = arr[i].capitalize()
        string += arr[i]

    string = string[: len(string) - 1]
    return string
