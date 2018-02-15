import sys
import getopt
from DeepLyricsGenerator import DeepLyricsGen

method = ''
filename = 'lyrics.txt'
epochs = 30
weight = ''

try:
    opts, args = getopt.getopt(sys.argv[1:],"hm:f:e:w:")
except getopt.GetoptError:
    print ('run.py -m <method (train|generate)> -f <textfile> -e <epochs> -w <weight>')
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        print ('run.py -m <method (train|generate)> -f <textfile> -e <epochs> -w <weight>')
        sys.exit()
    elif opt in ("-m"):
        method = arg
    elif opt in ("-f"):
        filename = arg
    elif opt in ("-e"):
        epochs = int(arg)
    elif opt in ("-w"):
        weight = arg

if not method:
    print ('Method not specified! Please specify argument -m train|generate')
    sys.exit()

generator = DeepLyricsGen(filename)

if method == 'generate':
    
    if not weight:
        print ('Weight not specified! You must specify a weight to generate texts: -w <weight>')
        sys.exit()

    generator.generate(weight)
elif method == 'train':
    generator.train(weight)
else:
    print ('Selecte train or generate to run')
    