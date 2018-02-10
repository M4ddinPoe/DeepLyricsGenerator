import sys
import numpy
import keras.backend
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint

class DeepLyricsGen:

    def __init__(self, filename):
        self.filename = filename
        self.filepath="weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
        self.words = []
        self.seq_length = 50
        self.dataX = []
        self.dataY = []

    def open_text(self):
        text = open(self.filename).read()
        text = text.lower()

        return text

    def create_chars_to_int_mappings(self, text):
        self.chars = sorted(list(set(text)))
        self.char_to_int = dict((c, i) for i, c in enumerate(self.chars))
        self.int_to_char = dict((i, c) for i, c in enumerate(self.chars))

    def summarize_data(self, text):
        self.n_chars = len(text)
        self.n_vocab = len(self.chars)
        print ("Total Characters: ", self.n_chars)
        print ("Total Vocab: ", self.n_vocab)

    def prepare_data(self, text):
        # prepare the dataset of input to output pairs encoded as integers
        seq_length = 100
        dataX = []
        dataY = []

        for i in range(0, self.n_chars - seq_length, 1):
            seq_in = text[i:i + seq_length]
            seq_out = text[i + seq_length]
            dataX.append([self.char_to_int[char] for char in seq_in])
            dataY.append(self.char_to_int[seq_out])

        n_patterns = len(dataX)
        print ("Total Patterns: ", n_patterns)

        # reshape X to be [samples, time steps, features]
        self.X = numpy.reshape(dataX, (n_patterns, seq_length, 1))

        # normalize
        self.X = self.X / float(self.n_vocab)

        # one hot encode the output variable
        self.y = np_utils.to_categorical(dataY)

    def create_model(self):
        model = Sequential()
        model.add(LSTM(512, input_shape=(self.X.shape[1], self.X.shape[2]), return_sequences=True))
        model.add(Dropout(0.4))
        model.add(LSTM(512))
        model.add(Dropout(0.4))
        model.add(Dense(self.y.shape[1], activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='Adadelta')

        return model

    def train(self):

        text = self.open_text()
        self.create_chars_to_int_mappings(text)
        self.summarize_data(text)
        self.prepare_data(text)

        model = self.create_model()

        checkpoint = ModelCheckpoint(self.filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
        callbacks_list = [checkpoint]

        # fit the model
        model.fit(self.X, self.y, epochs=30, batch_size=48, callbacks=callbacks_list)

    def generate(self, weight):

        text = self.open_text()
        self.create_chars_to_int_mappings(text)
        self.summarize_data(text)
        self.prepare_data(text) 

        model = self.create_model()

        model.load_weights(weight)
        model.compile(loss='categorical_crossentropy', optimizer='Adadelta')

        start = numpy.random.randint(0, len(self.dataX)-1)
        pattern = self.dataX[start]
        print ("Seed:")
        print ("\"", ''.join([self.int_to_char[value] for value in pattern]), "\"")

        # generate characters
        for i in range(150):
            x = numpy.reshape(pattern, (1, len(pattern), 1))
            x = x / float(self.n_vocab)
            prediction = model.predict(x, verbose=0)
            index = numpy.argmax(prediction)
            result = self.int_to_char[index]
            seq_in = [self.int_to_char[value] for value in pattern]
            sys.stdout.write(result)
            pattern.append(index)
            pattern = pattern[1:len(pattern)]

        print ("\nDone.")