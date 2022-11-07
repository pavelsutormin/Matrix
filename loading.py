from tqdm import tqdm
import time
from termcolor import colored
def load():
    try:
        for i in tqdm(range (100), 
                       desc="Loading…",
                       ascii=False, ncols=100, unit='bit', colour='GREEN'):
            i = colored(i,'green')
            time.sleep(0.05)
    except KeyboardInterrupt:
        exit