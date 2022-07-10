import requests
import json
import datetime
import deposit_to_mysql

bvIdList = ['BV17u411v7jn']

for i in bvIdList:
    url = "https://api.bilibili.com/x/web-interface/view?bvid=" + str(i)
    data = json.loads(requests.get(url).content.decode())['data']
    bvid = data['bvid']
    aid = data['aid']
    title = data['title']
    stat = data['stat']
    view = stat['view']
    reply = stat['reply']
    favorite = stat['favorite']
    coin = stat['coin']
    share = stat['share']
    now_rank = stat['now_rank']
    his_rank = stat['his_rank']
    like = stat['like']
    dislike = stat['dislike']
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql = """INSERT INTO video_info(bvid, aid, title, view, reply, favorite, coin, share, now_rank, his_rank, ulike, dislike, update_time, create_time) VALUES("{}",{},"{}",{},{},{},{},{},{},{},{},{},"{}","{}")""". \
        format(bvid, aid, title, view, reply, favorite, coin, share, now_rank, his_rank, like, dislike, dt, dt)
    deposit_to_mysql.bili_api_info_record(sql)