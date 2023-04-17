FROM mysql:8.0.32
ENV DEBIAN_FRONTEND=noninteractive

COPY my.cnf /etc/mysql/my.cnf
