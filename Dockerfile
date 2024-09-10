FROM python:3.11

WORKDIR /code

COPY src/fishregression/main.py /code/

# 모델서빙만 (의존성의 위 base이미지에서 모두 설치했다 )
# RUN pip install --upgrade git+https://github.com/baechu805/fishmlserv2.git@1.1.0/k
RUN pip install --upgrade git+https://github.com/baechu805/fishregression.git@0.2.0/cli

# 모델 서빙을 위해 API 구동을 위한 FASTAPI RUN
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
