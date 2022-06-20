FROM python:3.8-slim-buster

WORKDIR /app  

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY nsg.py .


EXPOSE 3001

CMD ["python", "nsg.py"]