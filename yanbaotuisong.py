#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
# @Author  : lusheng


from bs4 import BeautifulSoup
import urllib.request
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time


#研报下载
def report_download():
    # 万华研报列表地址
    urlbase = 'http://vip.stock.finance.sina.com.cn/q/go.php/vReport_List/kind/search/index.phtml?t1=2&symbol=600309&p='
    f = open('test.txt', 'w', encoding='utf-8')
    time1 = time.time()
    for i in range(1,6):
        url = urlbase + str(i)
        print('从第%d页下载研报清单' % i)
        # 下载网页
        req = urllib.request.Request(url)
        response1=urllib.request.urlopen(req)
        html=response1.read().decode('gbk')
        # print(html)

        #分析网页数据、获取研报地址
        soup = BeautifulSoup(html, "html.parser")
        # print(soup.prettify())
        lists = soup.find_all('td', class_="tal f14")
        # print(list)
        links = []
        for tag in lists:
            print(tag)
            link = tag.find('a').get('href')
            title = tag.find('a').get('title')
            # 链接全部存储在links列表中
            links.append(link)
            print(link, title)
    time2 = time.time()
    print(time2 - time1)

    #下载研报网页内容
    print(len(links))
    for link1 in links[0:5]:
        print(link1)
        req3 = urllib.request.Request(link1)
        response3 = urllib.request.urlopen(req3)
        html3 = response3.read().decode('gbk','ignore')
        # print(html3)
        soup3 = BeautifulSoup(html3, "html.parser")
        # print(soup3)
        ptitle = soup3.find_all('h1')
        pcontent = soup3.find_all('p')
        ptitle2 = str(ptitle)
        pcontent2 = str(pcontent)
        print(ptitle2,pcontent2)
        f.write(ptitle2)
        f.write('\n')
        f.write(pcontent2)
        f.write('\n\n')
    # 建立txt文件

    f.close()


# 发送研报
def send_report():
    mail_host="smtp.qq.com"  #设置服务器
    mail_user="228383562@qq.com"    #用户名
    mail_pass="waajnvtmdhiucbef"   #口令
    sender = '228383562@qq.com'
    receiversName = '个人邮箱'
    receivers = 'lusheng1234@126.com'
    now = time.localtime()
    date = time.strftime("%Y-%m-%d", now)
    print(receiversName, receivers)
    content = open('test.txt', encoding='utf-8').read()
    print(content)

    mail_msg = """
    <p> %s 万华化学研报 </p>
    <p> %s: </p>
    <p>这是Python 研报推送测试... </p>
    """ % (date, content)
    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = Header("万华研报", 'utf-8')
    message['To'] = Header("万华研报", 'utf-8')
    subject = 'Python 万华研报'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP('smtp.qq.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


report_download()
send_report()

