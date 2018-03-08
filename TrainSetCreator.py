import random
import time
from os import listdir
from os.path import isfile, join

targetfile = 'lyrics.txt'
mypath = 'Albums'
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

start = 0
end = len(files) - 1

milliseconds = int(round(time.time() * 1000))
random.seed(milliseconds)

while start < end:
    start = random.randint(start, start + 35)

    if start > end:
        start = end

    file = files[start]

    try:
        with open(mypath + '/' + file, 'r', encoding='Latin-1') as myfile:
            data = myfile.read()

        with open(targetfile, 'a') as myfile:
            myfile.write(data)

        print('Added ' + file)
    except:
        print('Could not read ' + file)
