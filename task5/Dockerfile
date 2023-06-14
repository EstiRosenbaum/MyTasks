# FROM node:latest
# WORKDIR /app
# COPY . /app/
# EXPOSE 3030/tcp
# EXPOSE 3030/udp
# USER 1000
# CMD ["node","index.js"]


FROM nginx:alpine

EXPOSE 8080
COPY nginx.conf /etc/nginx/
WORKDIR /www/data/
COPY index.html /www/data/
WORKDIR /tmp/logs/
ENV port=8080
RUN echo /www/data/index.html
RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*
VOLUME ["/www/data/"]
