FROM python:2.7.9

ADD . /opt

RUN pip install -r /opt/requirements.txt

WORKDIR /opt

CMD nosetests --with-xunit --xunit-file="/nosetests.xml"
