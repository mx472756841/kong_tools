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
                # row path + method
                paths = row["paths"]
                methods = row["methods"]
                for path in paths:
                    for method in methods:
                        finnaly_data[f"{method}:{path}"] = ""
            if not next:
                break
            url = f"http://localhost:8001{next}"
            resp = requests.get(url)

        with open("route.json", 'w') as f:
            f.write(finnaly_data)
