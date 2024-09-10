import requests
import json

def lr_api(length): # 길이를 입력받아 선형회귀 API에 요청보냄, FastAPI 서버의 /fish_ml_regression 엔드포인트로 HTTP GET 요청을 보내어 물고기의 무게를 예측하고, 결과를 반환
    headers = {
        'accept': 'application/json',
    }

    params = {
        'length': length,
    }

    response = requests.get('http://127.0.0.1:8000/fish_how_weight', params=params, headers=headers)
    data=json.loads(response.text)
    r=data['prediction'] # weight 반환
    return r

def knn_api(length,weight,n_neighbors=5): # 예측된 길이와 무게를 사용하여 KNN 기반 물고기 분류 API를 호출, FastAPI 서버의 /fish_ml_predictor 엔드포인트로 HTTP GET 요청을 보내어 물고기의 종류(예: 도미, 빙어)를 예측하고, 그 결과를 반환
    headers = {
        'accept': 'application/json',
    }

    params = {
        'n_neighbors': n_neighbors,
        'length': length,
        'weight': weight,
    }

    response = requests.get('http://127.0.0.1:8002/kind_fish', params=params, headers=headers) # FastAPI의 /fish_ml_predictor 엔드포인트로 호출
    data=json.loads(response.text)
    r=data['prediction']
    
    return r

def predict():
    length = float(input("물고기의 길이를 입력하세요: "))

    # weight 예측 선형회귀 API 호출
    weight = lr_api(length) # prediction 값을 weight으로 받음

    # 물고기 분류 API  호출
    fish_class = knn_api(length, weight, n_neighbors=5)

    print(f"length:{length} 물고기는 weight:{weight} 으로 예측되며 종류는 {fish_class} 입니다.")

# 이 블록은 파일이 직접 실행될 때만 실행됨
if __name__ == "__main__":
    predict()  # predict() 함수 자동 실행   


# predict()함수
# 물고기의 길이를 입력하면, 그 값을 기반으로 선형 회귀 API를 호출하여 물고기의 무게를 예측
# 예측된 무게와 입력된 길이를 사용하여 KNN API를 호출하고 물고기의 종류를 예측
# 최종적으로 물고기의 길이, 예측된 무게, 그리고 물고기의 종류를 출력
