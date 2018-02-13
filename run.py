import sys
import getopt
from DeepLyricsGenerator import DeepLyricsGen

method = sys.argv[1]
filename = "lyrics.txt"

if len(sys.argv) >= 3:
    filename = sys.argv[2]

weight = ""

if len(sys.argv) >= 4:
    weight = sys.argv[3]

generator = DeepLyricsGen(filename)

if sys.argv[1] == 'generate':
    generator.generate(weight)
elif sys.argv[1] == 'train':
    generator.train(weight)
else:
    print ('Selecte train or generate to run')
