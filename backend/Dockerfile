FROM python:3.10.10-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /backend

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./e_comm3rce .

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]