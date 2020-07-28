#!/usr/bin/python3
# -*- coding: utf-8
"""
@author: mx472756841@gmail.com
@file: http_log.py
@time: 2020/7/28 16:22
"""
import json
import logging

from flask import Blueprint, Response, request

from middleware.http_log import HttpLog

http_log_bp = Blueprint('http_log', __name__, url_prefix='/http_log')
logger = logging.getLogger("full_logger")
http_log_bp.before_request(HttpLog.before_request)


@http_log_bp.route('/post', methods=['POST'])
def post():
    """
    接收kong发送的http log格式，转存到elasticsearch数据中
    """
    try:
        return Response(json.dumps(request.json), mimetype='application/json')
    except:
        logger.exception("处理httplog失败")
        resp = {
            "code": 99,
            "message": "处理信息失败"
        }
        return Response(json.dumps(resp), mimetype='application/json')
