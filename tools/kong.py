import requests


def handler_route():
    """
    对kong的所有route生成字典
    uri+method构成一个功能说明
    """
    finnaly_data = {}
    url = "http://localhost:8001/routes"
    resp = requests.get(url)
    if resp.status_code == 200:
        while True:
            resp_data = resp.json()
            next = resp_data.get("next")
            data = resp_data.get("data", [])
            # 处理data
            for row in data:
                # method + route_id
                methods = row["methods"]
                for method in methods:
                    finnaly_data["{}:{}".format(method, row['id'])] = {"paths": row["paths"], "note": "",
                                                                       "service_id": row["service"]["id"]}
            if not next:
                break
            url = "http://localhost:8001{}".format(next)
            resp = requests.get(url)

        with open("route.json", 'w') as f:
            f.write("{}".format(finnaly_data))
