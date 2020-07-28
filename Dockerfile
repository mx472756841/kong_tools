FROM python:3.8-alpine3.9

# 构建redis
# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN addgroup -S redis && adduser -S -G redis redis

# 构建本地代码
COPY / /kong_tools/

WORKDIR /kong_tools/

RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 5000