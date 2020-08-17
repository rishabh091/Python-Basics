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


def combine_text(text_list):
    buffer = ''
    for i in text_list:
        buffer += i + ' '

    return buffer


# write in a demo file
def write_in_tmp(data_dict):
    file_name = 'tmp/{}'.format(random.random())
    with open(file_name, 'w') as file:
        file.write(json.dumps(data_dict))
    file.close()


# write result in .json file
def store_result(path, data):
    with open(path, 'w') as file:
        file.write(json.dumps(data))
    file.close()
