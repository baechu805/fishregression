from typing import Union
from fastapi import FastAPI
import pickle
import sys
#sys.path.append('/home/joo/code/fishregression/src/')

from fishregression.manager import get_model_path

app = FastAPI()

# 길이를 입력박아 예측된 무게 반환
def run_prediction(length:float): # 길이를 입력받음
    model_path = get_model_path() # 저장된 경로 반환
    with open(model_path, "rb") as f:
        fish_model = pickle.load(f) # 머신러닝 회귀모델 불러옴
    prediction = fish_model.predict([[length ** 2, length]]) # 예측 수행 (길이와 길이 제곱을 입력으로 사용)
    return float(prediction[0]) # 예측 결과 반환

@app.get("/")
def read_root():
    return {"Hello": "fish world"}


@app.get("/fish_how_weight")
def lr_api(length: float):
    """
    물고기의 무게를 예측하는 함수

    Args:
        length(float): 물고기의 길이(cm)
    
    Returns:
        dict:
            weight(float): 물고기 무게(g)
            length(flozt): 물고기 길이(cm)
    """
 ### 예측해서 결과 return
    prediction = run_prediction(length)
    
    return {
                "length":length,  # 입력된 물고기의 길이
                "prediction":prediction # 예측된 물고기의 무게
            }

