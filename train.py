import csv
import numpy as np
import keras
from model import Malconv
import sys
from dataset import MalwareDataset
input = sys.argv[1]

model : keras.Model = Malconv()
model.summary()


batch_size = 16
epochs = 5
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

"""
## Data will be read in the form of csv file
"""

dataset = MalwareDataset(input) 
       

model.fit(dataset,batch_size=batch_size, epochs=epochs, validation_split=0.1)
model.save("malconv.keras")