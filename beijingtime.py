import os
from datetime import datetime, timedelta


utc_now = datetime.utcnow()
bj_time = "\n北京时间\n" + str((utc_now + timedelta(hours=8)).strftime("%Y年%m月%d日%H时%M分%S秒"))



print(bj_time)
 
