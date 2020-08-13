import pdf2image
from PIL.PpmImagePlugin import PpmImageFile

import pdf_to_image.services as services

# get image
import pdf_to_image.getImage as get_image


# output path: pdf_to_image/output
# main process listed here
def process(pdf_path):
    # location where pdf is stored
    print('PDF Path : ', pdf_path)

    try:
        # use pdf2image to convert pdf in images
        images_from_path = pdf2image.convert_from_path(pdf_path)

        for image in images_from_path:
            # get the destination where you wanna store image
            name_of_file = services.get_name()
            # save the image
            PpmImageFile.save(image, format='jpeg', fp=name_of_file)
            print(name_of_file + ' Saved !!')
    except Exception as e:
        print(e)
    finally:
        print('Completed !!')


if __name__ == '__main__':
    # process(sys.argv[1])
    paths = ('output/Image1', 'output/Image2')
    get_image.main(paths)
