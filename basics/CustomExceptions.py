def foobar(x):
    if x > 20:
        raise Exception
    else:
        print(x)


try:
    foobar(4)
except:
    print('Exception occured')
else:
    print('No Errors !!')
finally:
    print('Code completed')
