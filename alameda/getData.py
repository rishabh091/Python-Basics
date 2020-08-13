from alameda import services


def get_data(dict_data):
    final_dict = dict(get_values(dict_data, 'provider name:', 'provider'))
    return final_dict


# get values via indexing
def get_values(dict_data, key, end_key):
    texts = dict_data['text']
    key_arr = key.split(' ')
    key_length = len(key_arr)

    result = {}

    for i in range(key_length, len(texts)):
        tmp_key = ''

        for j in range(key_length):
            tmp_key = texts[i - key_length - j - 1].lower() + ' ' + tmp_key

        if tmp_key.strip() == key:
            result[services.get_json_key(key)] = services.form_data(get_data_via_index(end_key, i - key_length, texts))

    return result


def get_data_via_index(end_statement, start_index, arr):
    result = []

    for i in range(start_index, len(arr)):
        string = arr[i].lower()

        if string != end_statement:
            result.append(arr[i])
        else:
            break

    return result
