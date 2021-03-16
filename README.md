# EasyPush
简单的微信推送方式集锦
## 企业微信应用推送
## pushplus推送
## Server酱推送

# 本地运行
1.  下载code。
2.  requirements.txt 是所需第三方模块，执行 `pip3 install -r requirements.txt` 安装模块。
3.  自行配置各种token或者key，ID,等。


# Github Actions说明
## 一、Fork此仓库
## 二、设置Secret
### Setting - Secrets - New Repository secret, Name填入变量名, Value填入变量值  
### **企业微信应用推送（可推送到微信）**  
wecomapp.py  
注册企业微信：https://work.weixin.qq.com  
进入管理后台-->选择应用管理-->选择创建应用-->填写应用名称  
创建好后，得到 AgentId 和 Secret 两个值  
回到企业微信后台，选择我的企业，翻到最底下，得到企业 ID  
添加名为**WWAPPID**的变量(AgentId的值）  
添加名为**WWAPPSECRET**的变量(Secret的值）  
添加名为**WWID**的变量(企业ID的值）  
添加名为**WWUSERID**的变量(可选，默认@all,用户ID）  
官方API文档：https://work.weixin.qq.com/api/doc/90001/90143/90372   
### **Server酱的推送**  
serverchan.py  
添加名为**SCKEY**的变量  
**SCKEY**  
KEY获取方法详见官网：https://sc.ftqq.com
### **Plushplus的推送**  
pushplus.py  
添加名为**PPTOKEN**的变量  
**PPTOKEN**  
TOKEN获取方法详见官网：http://pushplus.plus

## 三、ACTIONS


