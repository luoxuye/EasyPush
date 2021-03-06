# -*- codeing = utf-8 -*-
# @Author: Luo
# @Time : 2021-03-15 18:45:24

# 打开EasyPush/.github/workflows/EasyPush.yml或者自己的****/.github/workflows/***.yml文件
# 在env: 添加下面一行。
#         env:
#           SCKEY: ${{ secrets.SCKEY }}
import os
import requests
from datetime import datetime, timedelta

#北京时间
utc_now = datetime.utcnow()
bj_time = "  \n北京时间\n  " + str((utc_now + timedelta(hours=8)).strftime("%Y年%m月%d日%H时%M分%S秒"))

SCKEY = os.environ["SCKEY"] #本地运行时直接填具体"参数".

def severchan():
    pushdata = {
        "text": f"推送标题",
        "desp": "推送内容" + bj_time
    }
    res = requests.post(f"https://sctapi.ftqq.com/{SCKEY}.send", data=pushdata)
    print(res.text)
    
    
    
if SCKEY != "":
    severchan()

print("SCKEY = " + SCKEY)
print(bj_time)
