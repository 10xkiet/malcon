import numpy as np
def read_bytes(filepath, max_len=200000):
    with open(filepath, 'rb') as f:
        bytez = list(f.read())
    pad = max_len - len(bytez) % max_len    
    bytez += [0]*pad

    return np.array(bytez, dtype=np.uint8).reshape((-1,max_len))
