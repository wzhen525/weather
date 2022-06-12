# -*- coding: utf-8 -*-
"""
Created on Mon May 23 17:42:45 2022

@author: dell
"""

import pandas
import matplotlib.pyplot as plt

def tem_draw(data):
    #绘制温度曲线
    tem=list(data['温度'])
    hour=list(data['小时'])
    tem_avg=sum(tem)/24   #求平均温度
    tem_avg_list=[]
    x=[]
    y=[]
    for i in range(0,24):
        x.append(i)
        y.append(tem[hour.index(i)])#列表y存放与列表x相对应小时的温度
        tem_avg_list.append(tem_avg)
    plt.plot(x,y,color='red',label='温度')
    plt.plot(x,tem_avg_list,color='black',linestyle='--',label='平均温度')
    plt.scatter(x,y,color='red')
    plt.grid()
    plt.xticks(x)#定x轴刻度
    plt.title('一天的温度变化')
    plt.xlabel('时间/h')
    plt.ylabel('温度/℃')
    plt.legend()
    #plt.figure(1)
    plt.show()
def hum_draw(data):
    #绘制湿度曲线
    hum=list(data['相对湿度'])
    hour=list(data['小时'])
    hum_avg=sum(hum)/24   #求平均湿度
    hum_avg_list=[]
    x=[]
    y=[]
    for i in range(0,24):
        x.append(i)
        y.append(hum[hour.index(i)])
        hum_avg_list.append(hum_avg)
        
    plt.plot(x,y,color='blue',label='湿度')
    plt.plot(x,hum_avg_list,color='black',linestyle='--',label='平均湿度')
    plt.scatter(x,y,color='blue')
    plt.grid()
    plt.xticks(x)
    plt.title('一天的湿度变化')
    plt.xlabel('时间/h')
    plt.ylabel('湿度/℃')
    plt.legend()#为图表打标注
    
    plt.show()
def main():
    plt.rcParams['font.sans-serif']=['SimHei']	# 解决中文显示问题
    data1=pandas.read_csv('weather1.csv',encoding='gb2312')
    print(data1)
    tem_draw(data1)
    hum_draw(data1)
if __name__=='__main__':
    main()






