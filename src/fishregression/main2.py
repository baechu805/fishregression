from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# KNeighborsClassifier 모델 파일 경로
MODEL_PATH = "/home/joo/code/fishmlserv/note/model_knn.pkl"

# KNN 모델을 불러오는 함수
def load_model():
    with open(MODEL_PATH, "rb") as f:
        knn_model = pickle.load(f)
    return knn_model

# KNN 모델 불러오기
knn_model = load_model()

# 물고기 종류 예측 함수
def predict_fish_class(length: float, weight: float, n_neighbors: int = 5):
    # 입력된 길이와 무게를 기반으로 물고기의 종류를 예측
    data = np.array([[length, weight]])  # 길이와 무게를 입력으로 받음
    prediction = knn_model.predict(data)  # KNN 모델을 사용해 예측
    if prediction[0] == 1:
        return "도미"
    else:
        return "빙어"

@app.get("/")
def read_root():
    return {"Hello": "fish world"}

# 물고기 분류 API
@app.get("/kind_fish")
def fish_classifier_api(length: float, weight: float, n_neighbors: int = 5):
    """
    물고기의 길이와 예측된 무게를 받아 물고기의 종류를 예측하는 API.

    Args:
        length (float): 물고기의 길이(cm)
        weight (float): 예측된 물고기의 무게(g)
        n_neighbors (int): KNN에서 사용할 이웃의 수 (기본값: 5)

    Returns:
        dict:
            length (float): 입력된 물고기의 길이
            weight (float): 입력된 물고기의 무게
            prediction (str): 예측된 물고기의 종류 ('도미' 또는 '빙어')
    """
    fish_class = predict_fish_class(length, weight, n_neighbors)
    
    return {
        "length": length,
        "weight": weight,
        "prediction": fish_class
    }

