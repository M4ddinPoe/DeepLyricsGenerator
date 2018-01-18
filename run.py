import sys
from DeepLyricsGenerator import DeepLyricsGen

filename = "lyrics_very_small.txt"
generator = DeepLyricsGen(filename)

if sys.argv[1] == 'generate':
    filename = "weights-improvement-01-6.4272.hdf5"
    generator.generate(filename)
elif sys.argv[1] == 'train':
    generator.train()
else:
    print ('Selecte train or generate to run')