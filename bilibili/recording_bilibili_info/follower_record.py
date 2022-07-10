import requests
import json
import datetime
import deposit_to_mysql
# 填放uid
uidList = [153495223]
# 每个uid当前的粉丝数、偷偷关注、黑名单获取并且存放
for i in uidList:
    url = 'https://api.bilibili.com/x/relation/stat?vmid=' + str(i) + '&jsonp=jsonp'
    data = json.loads(requests.get(url).content.decode())['data']
    uid = data['mid']
    following = data['following']
    whisper = data['whisper']
    black = data['black']
    follower = data['follower']
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql = """INSERT INTO follow_info(uid, following, whisper, black, follower, update_time, create_time) VALUES({},{},{},{},{},"{}","{}")""". \
        format(uid, following, whisper, black, follower, dt, dt)
    deposit_to_mysql.bili_api_info_record(sql)