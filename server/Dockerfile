FROM ubuntu
MAINTAINER Andres Daille "andres.daille@mail.udp.cl"
MAINTAINER Tommy Rinaldi "tommy.rinaldi@mail.udp.cl"
WORKDIR /geodns

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update \
&& apt-get -y upgrade \
&& apt-get -y install build-essential \
&& apt-get -yqq install git golang pkg-config libssl-dev \
&& go get github.com/abh/geodns \
&& cd ~/go/src/github.com/abh/geodns \
&& go test \
&& go build
