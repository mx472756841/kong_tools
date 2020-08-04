import json
import traceback

from flask import request, current_app

from utils.amap import AMap

# example
ACTION_MAPPING = {
    'POST:74e1ac0a-a791-48bd-b362-c01e7e9dd294': {
        'paths': [
            '/test/v1/handle'],
        'note': '测试功能',
        'service_id': 'c9beb237-7e85-49b3-8561-0082fc8086ea'
    }

}


class HttpLog:

    @classmethod
    def _get_localtion_by_client_ip(cls):
        """
        根据client_ip 获取所在城市
        """
        request.json['localtion'] = {}
        try:
            ip = request.json['request']['headers']['x-real-ip']
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
            token = request.json["request"]["headers"].get("x-access-token", "")
            if token:
                user_key = current_app.config["USER_KEY"] % token
                data = current_app.redis.get(user_key)
                if data:
                    request.json['user'] = json.loads(data.decode("utf-8"))
        except:
            traceback.print_exc()

    @classmethod
    def _get_action_info(cls):
        request.json['action'] = ""
        try:
            request.json['action'] = ACTION_MAPPING.get(
                f"{request.json['request']['method']}:{request.json['route']['id']}", {}).get("note", "")

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
