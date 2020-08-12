import os.path


# counter
__image_counter = 0


def get_name():
    global __image_counter
    __image_counter += 1

    name_of_file = 'Image' + str(__image_counter)
    path = os.path.join('output', name_of_file)

    return path
