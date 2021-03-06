import argparse
import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("/content/drive/MyDrive/Datasets/Sheykh Recognizer.h5")

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--input', type=str ,help="Enter path of your image")

args = my_parser.parse_args()

width = height = 224

img = cv2.imread(args.input)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (width, height))
img = img / 255.0
img = img.reshape(1, width, height, 3)

result = model.predict(img)

pred = np.argmax(result)

if pred == 0:
  print("Normal")
elif pred == 1:
  print("Sheykh")
