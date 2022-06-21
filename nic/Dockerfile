FROM python:3.8-slim-buster

WORKDIR /app  

COPY requirements.txt .
RUN apt-get update

RUN apt-get -y install curl

RUN apt-get -y install sudo

RUN sudo curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

RUN pip install -r requirements.txt

COPY nic.py .


EXPOSE 3003

CMD ["python", "nic.py"]