#coding=utf-8
import requests
from spiderhelper import SpiderHelper
import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr


class ZhiHu:
    def __init__(self):
        self.spiderhelper = SpiderHelper() 
    def spider_zhihu(self):
        messages = ''
        datas = self.spiderhelper.get_datas()
        for data in datas:
            message = '<font color=red><b>'+'★  '+data['title']+':'+(data['href'])+'</b></font>'
            line = '<br></br>'
            messages += message
            messages += line
        return messages

def mail(sender,receiver,password,message):
    ret = True
    try:
        message = MIMEText(message,_subtype='html',_charset='utf-8') # 发送的内容
        message['Subject'] = '知乎好文'
        message['From'] = formataddr(['我的小肚腩。',sender])
        message['To'] = formataddr(['我的小肚腩。',receiver])
        server = smtplib.SMTP_SSL('smtp.qq.com',465)
        server.login(sender,password)
        server.sendmail(sender,[receiver,],message.as_string())
        print 'send message success'
        server.quit()
    except :
        print 'send message failed'
        ret =False
    return ret

def main():
    reload(sys)
    sys.setdefaultencoding('utf8')
    sender = '154290422@qq.com'
    receiver = '154290422@qq.com'
    password = 'qhmjlyjheeegbibh' # 生成的密码
    zhihu = ZhiHu()
    ret = mail(sender,receiver,password,zhihu.spider_zhihu())

if __name__ == '__main__':
    main()