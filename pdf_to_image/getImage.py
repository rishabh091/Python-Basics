import PIL.Image as Image
# pytesseract is a type of OCR library
import pytesseract
import cv2
import numpy


# re-reading image if stored in jpeg will change format from ppm image plugin to
# jpeg image plugin in PIL package
def main(paths: tuple):
    images = []

    for path in paths:
        image = Image.open(path)
        images.append(image)

        print(pytesseract.image_to_string(image))

    # data = pytesseract.image_to_data(images[0], output_type=pytesseract.Output.DICT)
    # boxes = len(data['level'])
    #
    # for i in range(boxes):
    #     (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
    #     cv2.rectangle(numpy.array(images[0]), (x, y), (x + width, y + height), (0, 255, 0), 2)
    #
    # cv2.imshow('img', images[0])
    # cv2.waitKey(0)
    #
    # print('Image Converted !!')
