# -*- coding: utf-8 -*-
"""
Created on Mon May 23 19:50:22 2022

@author: dell
"""


import matplotlib.pyplot as plt
import pandas

def tem_draw(data):
    tem_high=list(data['最高温度'])
    tem_low=list(data['最低温度'])
    
    day=[1,2,3,4,5,6,7]
    plt.plot(day,tem_high,color='red',label='高温')
    plt.plot(day,tem_low,color='blue',label='低温')
    
    plt.scatter(day,tem_high,color='red')
    plt.scatter(day,tem_low,color='blue')
    
    plt.grid()
    plt.legend()
    plt.xticks(day)
    plt.title('未来7天气温变化图')
    plt.xlabel('日期')
    plt.ylabel('温度')
    plt.show()
def main():
    plt.rcParams['font.sans-serif']=['SimHei']	# 解决中文显示问题
    data7=pandas.read_csv('weather7.csv',encoding='gb2312')
    print(data7)
    tem_draw(data7)
if __name__=='__main__':
    main()

