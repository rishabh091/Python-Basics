import io

filename = '/home/rishabh/Documents/Study/Major Security Threats of History.odt'

'''
StringIO() for string related streams and 
BytesIO() for bytes related streams
'''
try:
    buff = io.BytesIO()
    # file
    file = open(filename, 'r')
    print(file.read())
    buff.write(bytes(file.read()))

    print(buff.read())
except Exception as e:
    print(e)
