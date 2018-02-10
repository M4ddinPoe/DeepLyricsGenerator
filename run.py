import sys
from DeepLyricsGenerator import DeepLyricsGen

filename = "lyrics.txt"
generator = DeepLyricsGen(filename)

if sys.argv[1] == 'generate':
    filename = "output/weights-improvement-07-6.0545.hdf5"
    generator.generate(filename)
elif sys.argv[1] == 'train':
    generator.train()
else:
    print ('Selecte train or generate to run')