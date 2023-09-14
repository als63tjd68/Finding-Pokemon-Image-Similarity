import matplotlib.pyplot as plt
from load import load_data, FeatureExtractor

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
def main():
    # 데이터 로드
    img_paths, features = load_data()
    
    # 이미지 특징 추출 클래스 초기화
    fe = FeatureExtractor()
    
    # 쿼리 이미지 경로 설정
    query_image_path = "./pokemon/images/images/squirtle.png"
    
    # 쿼리 이미지 특징 추출
    query_img = Image.open(query_image_path)
    query_feature = fe.extract(query_img)
    
    # 유사도 계산 (코사인 유사도)
    cosine_sims = cosine_similarity(features, [query_feature])
    
    # 상위 30개 유사한 이미지 인덱스 가져오기
    similar_indices = np.argsort(cosine_sims[:, 0])[::-1][:30]
    
    # 결과 시각화
    axes = []
    fig = plt.figure(figsize=(8, 8))
    for a in range(5 * 6):
        index = similar_indices[a]
        score = cosine_sims[index][0]
        image_path = img_paths[index]
        axes.append(fig.add_subplot(5, 6, a + 1))
        subplot_title = f"Sim.: {score:.2f}"
        axes[-1].set_title(subplot_title)
        plt.axis('off')
        plt.imshow(Image.open(image_path))
    
    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
