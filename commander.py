import os
version = '1.0.0'
class MatrixError(OSError):
    def __init__(self, errno='',error=''):
        self.errormsg = error
        self.error = error
        self.strerror = error
        self.message = error
        self.errno = errno
def run(com,atr):
    if com == 'exit':
        os.system('clear')
        exit()
    elif com == 'input':
        input(atr)
    elif com == 'explode':
        print(atr+'\n')
    elif com == 'save':
        open('comm.com', 'a').write(atr+'\n')
    elif com == 'print':
        print(atr)
    elif com == 'clear':
        os.system('clear')
    elif com == '':
        pass
    else:
        print('command not found: '+com+' '+atr)

def find(string, char):
    string = str(string)
    f = string.find(char)
    if f == -1:
        return False
    else:
        return True