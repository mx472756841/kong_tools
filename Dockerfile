FROM python:3.6-alpine3.9

RUN apk add --no-cache \
'su-exec>=0.2' \
tzdata

# 构建本地代码
COPY / /kong_tools/

WORKDIR /kong_tools/

RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 5000
