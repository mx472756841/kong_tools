import json
import traceback

from flask import request, current_app

from utils.amap import AMap


class HttpLog:

    @classmethod
    def _get_localtion_by_client_ip(cls):
        """
        根据client_ip 获取所在城市
        """
        request.json['localtion'] = {}
        try:
            ip = request.json.get("client_ip")
            print(ip)
            if ip:
                rv, state_code = AMap().get_place_by_ip(ip, current_app.config["AMAP_KEY"])
                if state_code == 200 and isinstance(rv, dict) and str(rv.get("status")) == '1':
                    request.json['localtion'] = rv
        except:
            traceback.print_exc()

    @classmethod
    def _get_user_info(cls):
        request.json['user'] = {}
        try:
            token = request.json.get("request", {}).get("headers", {}).get("X-Access-Token")
            if token:
                data = current_app.admin.redis.get(token)
                if data:
                    request.json['user'] = json.loads(data.decode("utf-8"))
        except:
            traceback.print_exc()

    @classmethod
    def _get_action_info(cls):
        request.json['action'] = ''
        try:
            request.json['action'] = ""
        except:
            traceback.print_exc()

    @classmethod
    def before_request(cls):
        """
        每次请求前处理的事情
        """
        cls._get_localtion_by_client_ip()
        cls._get_user_info()
        cls._get_action_info()