FROM python:3.8-slim-buster

WORKDIR /app  

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY publicip.py .


EXPOSE 3002

CMD ["python", "publicip.py"]