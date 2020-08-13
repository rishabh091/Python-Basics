import PIL.Image as Image
# pytesseract is a type of OCR library
import pytesseract


# re-reading image if stored in jpeg will change format from ppm image plugin to
# jpeg image plugin in PIL package
def main(paths: tuple):
    images = []

    for path in paths:
        image = Image.open(path)
        images.append(image)

    

    # data_dict = pytesseract.image_to_data(images[0], output_type=pytesseract.Output.DICT)
    #
    # print('Getting data....')
    # result = {}
    # text_list = data_dict['text']
    # # convert whole list in lowercase
    # text_list = [i.lower() for i in text_list]
    # start_pointer = 0
    # total_words = len(text_list)
    # temp = ''
    #
    # print('Total Words in document : ', total_words)
    #
    # while start_pointer < total_words:
    #
    #     if text_list[start_pointer] == 'remittance':
    #         # because first word is remittance and we wont want that
    #         start_pointer += 1
    #
    #         while start_pointer < total_words and text_list[start_pointer] != 'date:':
    #             temp += text_list[start_pointer] + " "
    #             start_pointer += 1
    #
    #         temp = temp.strip()
    #         result['Provider'] = temp
    #         temp = ''
    #     if text_list[start_pointer] == 'date:':
    #         start_pointer += 1
    #         result['Date'] = text_list[start_pointer]
    #
    #     start_pointer += 1
    #
    # print(result)

    # levels = len(data_dict['level'])
    #
    # print('Levels : ', levels)
    # print('Left : ', len(data_dict['left']))
    # print('Top : ', len(data_dict['top']))
    # print('Width : ', len(data_dict['width']))
    # print('Height : ', len(data_dict['height']))
    #
    # num_img = np.asarray(images[0])
    #
    # # just for demonstration purpose
    # # create rectangle against all the texts
    # for i in range(levels - 1):
    #     (x, y, w, h) = (data_dict['left'][i], data_dict['top'][i], data_dict['width'][i], data_dict['height'][i])
    #     cv2.rectangle(num_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #
    # cv2.resize(num_img, (1200, 786))
    # cv2.imwrite('output/cv.jpeg', num_img)
    # cv2.waitKey(0)
    print('Finished !!')

