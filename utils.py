import numpy as np
def read_bytes(filepath, max_len=200000):
    with open(filepath, 'rb') as f:
        bytez = list(f.read())
        
    if len(bytez) < max_len:
        bytez += [0] * (max_len - len(bytez))
    else:
        bytez = bytez[:max_len]

    return np.array(bytez, dtype=np.uint8)