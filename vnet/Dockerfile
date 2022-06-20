FROM python:3.8-slim-buster

WORKDIR /app  

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY vnet.py .


EXPOSE 3000

CMD ["python", "vnet.py"]