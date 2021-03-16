# -*- codeing = utf-8 -*-
# @Author: Luo
# @Time : 2021-03-15 18:45:24

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
PPTOKEN = os.environ["PPTOKEN"] #本地运行时直接填具体"参数".
def pushplus():
    pushdata = {
        "title": f"推送的标题",
        "content": f"  \n推送的内容\n  "+ bj_time,
        "template":"markdown"
    }
    if PPTOKEN != "":
        return requests.post(f"http://www.pushplus.plus/send?token={PPTOKEN}", data=pushdata)
    else:
        return False
    
  
if PPTOKEN:
    pushplus()

print("PPTOKEN = " + PPTOKEN)



 
 


