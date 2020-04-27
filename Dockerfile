FROM python:3.8
ENV PYTHONNUNBEFFERED 1
WORKDIR /opt/federation
ADD requirements.txt /opt/federation
RUN pip3 install -r requirements.txt
ADD . /opt/federation
EXPOSE 8000


