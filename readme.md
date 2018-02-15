# Deep Learning Generator
## My First Deep Learning Project

This are my first steps into deep learning. This Code is based on the blog post from Jason Brownlee (https://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/).

This a text generating LSTM neural network trained on Heavy Metal lyrics.

## Prerequisites
Install Tensorflow and Kers
- https://www.tensorflow.org/
- https://keras.io/

## How to start
`run.py -m <method (train|generate)> -f <textfile> -e <epochs> -w <weight>`

**method:** 'train' to train a new model 
        'generate' to generate lyrics with a trained model
        
**textfile:** the textfile with the text to train

**epochs:** Number of epchos that the model will be trained

**weights:** the saved weight for a model to generate text
