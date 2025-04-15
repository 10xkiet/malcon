import keras
from model import Malconv
model = keras.models.load_model("malconv_ember.h5",compile=False)
model.summary()
malconv=Malconv()
malconv.summary()