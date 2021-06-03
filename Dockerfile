FROM ubuntu:18.04
EXPOSE 8000

RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip mysql-server cmake ffmpeg libsm6 libxext6 nginx
RUN python3 -m pip install -U pip
RUN python3 -m pip install -U setuptools

ADD schema.sql /schema.sql
ADD nginx-configuration /etc/nginx/sites-enabled/faces
RUN service nginx reload
RUN mysql < schema.sql
ADD ./Daemon /Daemon
ADD ./Server /Server

WORKDIR /Daemon
RUN python3 -m pip install -r requirements.txt 
WORKDIR /Server
RUN python3 -m pip install -r requirements.txt

WORKDIR /Daemon
CMD python3 run.py & bg

WORKDIR /Server
CMD python3 debug.py & bg
