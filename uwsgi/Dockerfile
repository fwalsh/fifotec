FROM python:2.7.9

RUN pip install uwsgi==2.0.9 Flask==0.10.1 nose==1.3.4

ADD . /opt/app

RUN pip install -r /opt/app/requirements.txt

EXPOSE 8001

CMD uwsgi /opt/app/hello.ini