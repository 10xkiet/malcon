from keras import layers , models
def Malconv(max_len=200000, win_size=500, vocab_size=256):    
    inp = layers.Input((max_len,))
    emb = layers.Embedding(vocab_size, 8)(inp)

    conv1 = layers.Conv1D(kernel_size=(win_size), filters=128, strides=(win_size), padding='same')(emb)
    conv2 = layers.Conv1D(kernel_size=(win_size), filters=128, strides=(win_size), padding='same')(emb)
    a = layers.Activation('sigmoid', name='sigmoid')(conv2)
    
    mul = layers.multiply([conv1, a])
    a = layers.Activation('relu', name='relu')(mul)
    p = layers.GlobalMaxPool1D()(a)
    d = layers.Dense(64)(p)
    out = layers.Dense(1, activation='sigmoid')(d)

    return models.Model(inp, out)