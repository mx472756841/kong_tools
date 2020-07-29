#!/usr/bin/python3
# -*- coding: utf-8
"""
@author: mx472756841@gmail.com
@file: http_log.py
@time: 2020/7/28 16:22
"""
import json
import logging

from elasticsearch import Elasticsearch
from flask import Blueprint, Response, request, current_app

from middleware.http_log import HttpLog

http_log_bp = Blueprint('http_log', __name__, url_prefix='/http_log')
logger = logging.getLogger("full_logger")
http_log_bp.before_request(HttpLog.before_request)


@http_log_bp.route('/post', methods=['POST'])
def post():
    """
    接收kong发送的http log格式，转存到elasticsearch数据中
    """
    resp = {
        "code": 0,
        "message": "处理成功"
    }
    try:
        # 将内容转发至elasticsearch
        es_service = Elasticsearch([current_app.config['ELASTICSEARCH_URL']])
        update_data = {
            "doc": request.json,
            "doc_as_upsert": True
        }
        rv = es_service.index("", update_data)
        logger.info("rv >>>> {} ".format(rv))
    except:
        logger.exception("处理httplog失败")
        resp["code"] = 99
        resp["message"] = "处理信息失败"
    return Response(json.dumps(resp), mimetype='application/json')
