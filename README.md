# kong tools

## 构建原理
Kong网关的工具

[*] httplog插件扩展，将日志内容发送到elasticsearch中

[ ] 扩展插件，根据ip地址获取所在地

[ ] 扩展插件，根据请求URL+GET获取到功能属性

[ ] 扩展插件，提取用户信息

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
    --name kong_tools kong_tools
```

## 使用
```shell
curl -i -X POST \
    -H 'Content-Type: application/json' \
    -H 'AccessToken: mSnbqTHqfIG6fIq6' \
    --url http://localhost:10050/wechat/send \
    -d '{"msg_type": "text","send_data": {"text": {"content": "测试消息"}},"to_users": ["要发送的用户"]}'
```

