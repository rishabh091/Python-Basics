import os

fileName = 'DemoText.txt'

file = None
try:
    # create empty File
    file = open(fileName, 'x')
    print('File Created')
except:
    print('File already created deleting and creating a new one')

    if os.path.exists(fileName):
        os.remove(fileName)
    print('File Deleted')
finally:
    if not os.path.exists(fileName):
        file = open(fileName, 'x')
        print('File Created')

    # write in file
    file.write('Hello World')
    print('File Written')
    file.close()

    file = open(fileName, 'r')
    # read that file
    print(file.read())
    file.close()
