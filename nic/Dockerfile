FROM python:3.8-slim-buster

WORKDIR /app  

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY nic.py .


EXPOSE 3003

CMD ["python", "nic.py"]