import numpy as np
from os import path
from PIL import Image
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.models import Model
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

class FeatureExtractor:
    def __init__(self):
        base_model = VGG16(weights='imagenet')
        self.model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc1').output)

    def extract(self, img):
        img = img.resize((224, 224))
        img = img.convert('RGB')
        x = image.img_to_array(img)
        x = preprocess_input(np.expand_dims(x, axis=0))
        feature = self.model.predict(x)[0]
        return feature / np.linalg.norm(feature)

def load_data():
    df = pd.read_csv("./pokemon/pokemon.csv")
    img_paths = []
    features = []
    fe = FeatureExtractor()
    for i in df['Name']:
        image_path = f"./pokemon/images/images/{i}.png"
        if not path.exists(image_path):
            image_path = f"./pokemon/images/images/{i}.jpg"
        img = Image.open(image_path)
        feature = fe.extract(img)
        img_paths.append(image_path)
        features.append(feature)
    return img_paths, features
