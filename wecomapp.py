# -*- codeing = utf-8 -*-
# @Author: Luo
# @Time : 2021-03-15 18:47:04
import os
import requests
import json
from datetime import datetime, timedelta

WWID = os.environ["WWID"] #本地运行时直接填具体"参数".
WWAPPSECRET = os.environ["WWAPPSECRET"] #本地运行时直接填具体"参数".
WWAPPID = os.environ["WWAPPID"] #本地运行时直接填具体"参数".
WWUSERID = os.environ["WWUSERID"] #本地运行时直接填具体"参数".选填
if WWUSERID == "":
    WWUSERID = "@all"
 
#北京时间
utc_now = datetime.utcnow()
bj_time = "  \n北京时间\n  " + str((utc_now + timedelta(hours=8)).strftime("%Y年%m月%d日%H时%M分%S秒"))





def access_token():
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?" + "corpid=" + WWID + "&corpsecret=" + WWAPPSECRET
    response = requests.get(url).json()
    access_token = response['access_token']
    return access_token
  


def wecom():
    pushdata = {
      "touser": WWUSERID,
      "toparty": "@all",
      "totag": "@all",
      "msgtype": "text",
      "agentid": WWAPPID,
      "text": {
          "content": "推送标题\n  " + "推送内容\n  " + bj_time
      },
      "safe": 0,
      "enable_id_trans": 0,
      "enable_duplicate_check": 0,
      "duplicate_check_interval": 1800
    }
    
    
    pushdata = json.dumps(pushdata)
  
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + access_token()
    res = requests.post(url=url, data=pushdata)
    print(res.text)
  
if WWID != "" and WWAPPSECRET != "" and WWAPPID != "":
  wecom()

print("WWID = " + WWID )
print("WWAPPSECRET = " + WWAPPSECRET )
print("WWAPPID = " + WWAPPID )
print(bj_time)

