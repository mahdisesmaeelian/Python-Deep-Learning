import argparse
import cv2
import numpy as np
from tensorflow.keras.models import load_weights

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--input_photo', type=str ,help="Enter path of your image")
my_parser.add_argument('--input_weights', type=str ,help="Enter path of your model")

args = my_parser.parse_args()

model = load_weights(args.input_weights)

width = height = 224

img = cv2.imread(args.input_photo)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (width, height))
img = img / 255.0
img = img.reshape(1, width, height, 3)

result = model.predict(img)

pred = np.argmax(result)

faces= ["Ali Khamenei","Angelina Jolie","Barak Obama","Behnam Bani","Donald Trump","Emma Watson","Han Hye Jin","Kim Jong Un",
"Leyla Hatami","Lionel Messi","Michelle Obama","Morgan Freeman","Queen Elizabeth","Scarlett Johanson"]

print(faces[pred])