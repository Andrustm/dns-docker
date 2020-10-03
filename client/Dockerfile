FROM ubuntu
MAINTAINER Andres Daille "andres.daille@mail.udp.cl"
MAINTAINER Tommy Rinaldi "tommy.rinaldi@mail.udp.cl"
WORKDIR /cliente

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update \
&& apt-get -y upgrade \
&& apt-get -y install build-essential \
&& apt-get -yqq install dnsutils pkg-config libssl-dev


ENTRYPOINT ["cliente"]
