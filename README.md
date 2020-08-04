# kong tools

## 构建原理
Kong网关的工具

- [x]  扩展插件，根据ip地址+高德地图获取所在地

- [x]  扩展插件，根据请求GET+ROUTE_ID获取到功能属性

- [x]  扩展插件，提取用户信息

- [x]  httplog 插件扩展，将日志内容添加到elasticsearch

## 部署
### virtualenv部署

1. virtualenv -p python3.6 venv
2. . venv/bin/activate
3. pip install -r requirements.txt
4. gunicorn -c etc/gunicorn.py manage:app

### docker部署
这里没有提供docker镜像，可直接使用Dockerfile从本地生成镜像即可
- 生成镜像
```shell
# 在当前目录执行以下命令
docker build -t kong_tools:latest .
```
- 启动服务

生成镜像之后启动镜像即可
```shell
docker run -p 10050:5000 -i -t -d \
--env REDIS_HOST=REDIS服务地址 \
--env REDIS_PORT=REDIS端口 \
--env REDIS_PASS=REDIS密码 \
--env REDIS_DB="REDIS DB" \
--env AMAP_KEY="高德地图的KEY" \
--env ELASTICSEARCH_URL="请求的elastic search地址" \
--name kong_tools kong_tools
```

