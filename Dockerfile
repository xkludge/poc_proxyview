FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /opt/identity
WORKDIR /opt/identity
COPY requirements.txt /opt/identity
RUN pip install -r requirements.txt
COPY app /opt/identity/
