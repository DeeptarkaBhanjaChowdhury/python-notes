from email import message


message = 'global'


def enclosing():
    message = 'enclosing'

    def local():
        # global message
        nonlocal message
        message = 'local'

    print('enclosing msg', message)
    local()
    print('enclosing msg', message)


print('global msg', message)
enclosing()
print('global msg', message)
