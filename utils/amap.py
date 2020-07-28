from utils.base import BaseRequest


class AMap(BaseRequest):
    """
    高德地图处理
    """

    def get_place_by_ip(self, ip, key):
        url = f"https://restapi.amap.com/v3/ip?ip={ip}&output=json&key={key}"
        return self.req_get(url)
