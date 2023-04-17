FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN echo 'root:docker123' | chpasswd
RUN sed -i 's@archive.ubuntu.com@mirror.kakao.com@g' /etc/apt/sources.list
RUN apt update && \
    apt install -y --no-install-recommends software-properties-common \
    sudo vim curl git python3 python3.8-venv python3-dev libmysqlclient-dev gcc

WORKDIR /scrap

RUN adduser --disabled-password --gecos "" scv

ENTRYPOINT bash
