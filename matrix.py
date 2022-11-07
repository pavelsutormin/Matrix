import termcolor
import commander
import os
def matrix():
    os.system('clear')
    termcolor.cprint('Matrix '+str(commander.version), 'white')
    while True:
        try:
            com = input(termcolor.colored('>>> ', 'green'))
            if commander.find(com, ' '):
                comm = com.split(' ')
            else:
                comm = [com, '']
            commander.run(comm[0],comm[1])
        except KeyboardInterrupt:
            break
    os.system('clear')
    exit()
