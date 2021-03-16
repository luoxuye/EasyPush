# Luo
# Time: 2021-03-15 18:32:17


# 打开EasyPush/.github/workflows/EasyPush.yml或者自己的****/.github/workflows/***.yml文件
# 在env: 添加下面一行。
#         env:
#           PPTOKEN: ${{ secrets.PPTOKEN }}
import os
import requests
from datetime import datetime, timedelta

utc_now = datetime.utcnow()
bj_time = "\n北京时间\n" + str((utc_now + timedelta(hours=8)).strftime("%Y年%m月%d日%H时%M分%S秒"))

print(bj_time)

#PPTOKEN = ""
PPTOKEN = ""
def pushplus(data):
    if PPTOKEN != "":
        return requests.post(f"http://www.pushplus.plus/send?token={PPTOKEN}", data=data)
    else:
        return False

pushplus({
    "title": "推送的标题",
    "content": "  \n推送的内容\n  "+ bj_time,
    "template":"markdown"
})




 
 


