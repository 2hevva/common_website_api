import requests
import json
import asyncio
# 用这个脚本去搜寻包含某些关键字标题的直播间，因为b站分类功能薄弱，还可以寻找同行观察和学习，也可以方便的找他们玩
url = """https://api.live.bilibili.com/xlive/web-interface/v1/second/getList?platform=web&parent_area_id=2&area_id=86&sort_type=sort_type_123&page={}"""
respondObjectList = []
for i in range(1, 50):
    for j in dict(json.loads(requests.get(url.format(i)).content.decode()))['data']['list']:
        # 筛选关键词在这
        if '斗' in j['title']:
            respondObjectList.append(j['roomid'])
    asyncio.sleep(1)
[print("""http://live.bilibili.com/{}""".format(i)) for i in respondObjectList]