import requests
# import os
#  “noaa_gfs_global_sflux_0.12d”は気象データのID
# os.environ["http_proxy"] = "http://konishi.kenji.z8%40tex-sol.com:pass@@19@172.16.16.3:15080/"
url = "http://api.planetos.com/v1/datasets/noaa_gfs_global_sflux_0.12d/point"
querystring = {
    "lat": "35.70",
    "lon": "139.80",
    "var": "Temperature_surface",
    "count": "500",
    "apikey": "4a758b79cbb4434d8fe3a598d2e13381",  # 2019/07/03
}
proxies = {
    'http': 'http://konishi.kenji.z8%40tex-sol.com:pass@@19@172.16.16.3:15080/',
    'https': 'http://konishi.kenji.z8%40tex-sol.com:pass@@19@172.16.16.3:15080/',
}
#    "apikey": "xxxx"               # xxxxはアカウント設定で取得したAPIキー
# response = requests.request(“GET”, url, params=querystring)
# 記載方法が変わった模様
# response = requests.get(url, params=querystring)
# proxy情報を追加
response = requests.get(url, params=querystring, proxies=proxies)
