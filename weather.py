# -*- coding: utf-8 -*-
"""
Created on Sat May 21 10:50:28 2022

@author: dell
"""


import requests
from bs4 import BeautifulSoup
from lxml import etree
import csv
import json

def get_url(url):
    r=requests.get(url)
    r.raise_for_status()
    #r.encoding=r.apparent_encoding
    data=r.content.decode('utf-8')
    return data

def get_data(data):
    text=etree.HTML(data)
    text_1=text.xpath('//div[@id="7d"]/ul/li')
    # 爬取7天内的天气状况
    weather_list=[]
    for i in text_1:
        day=i.xpath('.//h1/text()')[0]
        if i.xpath('.//p[@class="tem"]/span/text()'):
            tem_high=i.xpath('.//p[@class="tem"]/span/text()')
        else:
            tem_high=i.xpath('.//p[@class="tem"]/i/text()').extract_first()
        tem_low_1=i.xpath('.//p[@class="tem"]/i/text()')
        tem_low=list(map(lambda x:x.strip(),tem_low_1))
        weather_list.append([day[0],tem_high[0],str(tem_low[0][0:-1])])
    #爬取当天的天气情况
    weather_list2=[]
    bs=BeautifulSoup(data,features="lxml")
    body=bs.body
    #content=body.find('div',{'id':'7d'})
    content2=body.find_all('div',{'class':'left-div'})
    text=content2[2].find('script').string
    text=text[text.index('=')+1:-2]
    jd=json.loads(text)
    dayone=jd['od']['od2']
    count=0
    for i in dayone:
        temp=[]
        if count<=23:
            temp.append(i['od21'])#时间
            temp.append(i['od22'])#当前时刻温度
            temp.append(i['od27'])#当前时刻湿度
            #print(temp)
            weather_list2.append(temp)
        count+=1
    return weather_list,weather_list2

def write_to_csv(file_name,data,day=7):
    #将数据保存为csv文件
    with open(file_name,'w',newline="")as f:
        if day==1:
            headers=['小时','温度','相对湿度']
        else:
            headers=['日期','最高温度','最低温度']
        f_csv=csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(data)

def main():
    #主函数
    url='http://www.weather.com.cn/weather/101200101.shtml'
    data=get_url(url)
    data7,data1=get_data(data)
    
    print(data7)
    write_to_csv('weather7.csv',data7,7)
    write_to_csv('weather1.csv',data1,1)
if __name__=='__main__':
    main()
    


