import sys
import threads
from alameda import services
from alameda import getData


def process(path):
    print('Path of PDF : ', path)

    # get image from pdf
    images = services.convert_to_image(path)
    print(path, ' converted to Images !!')
    # convert image to dictionary via OCR
    print('Converting images to data...')
    result = []
    for image in images:
        data_dict = services.get_data_as_dict(image)
        data_string = services.combine_text(data_dict['text'])

        # just for demo purpose, comment this when not in use
        # services.write_in_tmp(data_dict)

        # extract data from dictionary
        print('For Image {}'.format(images.index(image) + 1))
        result.append(getData.get_data(data_dict, data_string))

    print('Result : ', result)
    services.store_result('tmp/result.json', result)


if __name__ == '__main__':
    process(sys.argv[1])
