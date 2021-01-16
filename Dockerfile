FROM python:latest

MAINTAINER aganapathy@hbs.edu

RUN apt-get update && apt-get -y install vim

RUN mkdir /automation

COPY ./Project /automation/Project
COPY ./setup.py /automation

WORKDIR /automation

RUN python3 setup.py install
RUN apt-get install sudo
RUN sudo apt-get install -y alien
RUN wget -c https://download.oracle.com/otn_software/linux/instantclient/211000/oracle-instantclient-basic-21.1.0.0.0-1.x86_64.rpm
RUN sudo alien -i *.rpm
RUN apt-get install libaio1