FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src .

EXPOSE 5006

CMD python server.py
