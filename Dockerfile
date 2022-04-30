# RoboCIn SoccerAnalyzer
# Author: Felipe Nunes
# Build command: sudo docker build . -t socceranalyzer
# Run command: sudo docker run -it

# Base image
FROM ubuntu:20.04

# Installation
RUN \
    add-apt-repository ppa:deadsnakes/ppa &&\
    apt-get update &&\
    apt-get -y upgrade &&\
    apt-get install -y python3.10 &&\
    apt-get install python3-pip

RUN \
    git clone https://github.com/robocin/SoccerAnalyzer.git
    cd SoccerAnalyzer
    pip3 install .

WORKDIR
    /root/SoccerAnalyzer

CMD ["bash"]