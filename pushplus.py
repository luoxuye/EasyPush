from datetime import datetime, timedelta
import requests

utc_now = datetime.utcnow()
bj_time = "\n北京时间\n" + str((utc_now + timedelta(hours=8)).strftime("%Y年%m月%d日%H时%M分%S秒"))

print(bj_time)

#token = ""
token = ""
def pushplus(data):
    if token != "":
        return requests.post(f"http://www.pushplus.plus/send?token={token}", data=data)
    else:
        return False

pushplus({
    "title": "推送的标题",
    "content": "  \n推送的内容\n  "+ bj_time,
    "template":"markdown"
})




 
 


