#!/usr/bin/python3
# -*- coding: utf-8
""" 
@author: mx472756841@gmail.com
@file: __init__.py
@time: 2019/5/6 14:52
"""
import os

from flask import Flask

from config import config
from .http_log import http_log_bp


def create_app():
    app = Flask(__name__)
    config_name = os.getenv('FLASK_CONFIG') or 'default'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.register_blueprint(http_log_bp)
    return app
