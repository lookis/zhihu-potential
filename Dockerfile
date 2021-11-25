# FROM docker.mirrors.ustc.edu.cn/library/python:3.8 as base
FROM python:3.8 as base
# FROM docker.mirrors.ustc.edu.cn/library/python:3.8-slim as container
FROM python:3.8-slim as container

FROM base as builder

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /
RUN pip install -r /requirements.txt --prefix=/install -i https://mirrors.aliyun.com/pypi/simple/

FROM container
EXPOSE 80
COPY --from=builder /install /usr/local
COPY . /app


WORKDIR /app

CMD ["scrapy", "crawl", "zhihu-potential"]