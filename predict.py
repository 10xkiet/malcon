from utils import read_bytes
import keras
import argparse
import os
parser = argparse.ArgumentParser("Prediction")
parser.add_argument("-m","--model")
parser.add_argument("-f","--filename")
parser.add_argument("-t","--threshold")
args = parser.parse_args()

model_path=args.model 
model=keras.models.load_model(model_path,compile=False)
input = args.filename 
threshold = int(args.threshold)
if os.path.isfile(input):
    x=read_bytes(input,1048576)
    x=x.reshape(1,-1)
    prediction=model.predict(x)[0][0]   
    confidence=prediction*100
    if confidence >= threshold:
        print(f"Malware detected. Confidence {confidence:.2f}%")
    else:
        print(f"Benign file. Confidence {100-confidence:.2f}%")
    