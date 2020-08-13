import json


if __name__ == '__main__':
    file = open('/home/rishabh/Downloads/jsonformatter.txt')
    data = file.read()

    data_as_dict = json.loads(data.encode().decode('utf-8-sig'))
    text_list = data_as_dict['text']

    while True:
        search_param = input('Enter Search Param : ')
        index = None
        for i, j in zip(text_list, enumerate(text_list)):
            if i.lower() == search_param:
                index = j[0]
                break

        if index is not None:
            print('Text : ' + list(data_as_dict['text'])[index])
            print('Page num : ', data_as_dict['page_num'][index])
            print('Block num : ', data_as_dict['block_num'][index])
            print('Par num : ', data_as_dict['par_num'][index])
            print('Left : ', data_as_dict['left'][index])
            print('Top : ', data_as_dict['top'][index])
            print('Width : ', data_as_dict['width'][index])
            print('Height : ', data_as_dict['height'][index])
        else:
            print('Data not found')
