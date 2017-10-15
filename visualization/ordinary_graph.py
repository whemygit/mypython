#!/usr/bin/env python
# -- coding: utf-8 --
import sys
from matplotlib import pyplot as plt
from pylab import *
import numpy as np
import datetime
from matplotlib import patheffects

reload(sys)
sys.setdefaultencoding("utf-8")

def fund_graph():
    # # 单变量线形图
    # # plt.plot([1,2,3,2,3,2,2,1])
    # # plt.show()
    # # 两变量线形图
    # # plt.plot([4,3,2,1],[1,2,3,4]) #第一个列表为横轴，第二个列表为纵轴
    # # plt.show()
    #
    # #基于相同数据生成一些常见图表###############################################
    # #some simple data
    # x=[1,2,3,4]
    # y=[5,4,3,2]
    #
    # #create new figure
    # plt.figure()
    #
    # #divide subplots into 2*3 grid and select #1
    # plt.subplot(231)
    # plt.plot(x,y)
    # # plt.show()
    #
    # #select #2
    # plt.subplot(232)
    # plt.bar(x,y)
    # # plt.show()
    #
    # #select #3
    # #horizontal bar-charts
    # plt.subplot(233)
    # plt.barh(x,y)
    # # plt.show()
    #
    # #create stacked bat charts,把连个柱状图调用连在一起，y轴为多变量的叠加，各用不同颜色显示
    # plt.subplot(234)
    # plt.bar(x,y)
    # y1=[7,8,5,3]
    # plt.bar(x,y1,bottom=y,color='r')
    # # plt.show()

    # box plot,boxplot适用于单变量
    # plt.subplot(235)
    # plt.boxplot(x)
    # plt.show()

    #scatter plot
    # plt.subplot(236)
    # plt.scatter(x,y)
    # plt.show()


    #箱线图和直方图####################################################################
    dataset=[
        113,115,119.121,124,
        124,125,126,126,126,
        127,127,128,129,130,
        130,131,132,133,136
    ]

    # plt.subplot(121)
    # plt.boxplot(dataset,vert=False)
    # plt.subplot(122)
    # plt.hist(dataset)
    # plt.show()


    # #sin and cos#########################################################################
    # x=np.linspace(-np.pi,np.pi,256,endpoint=True)
    # y=np.cos(x)
    # y1=np.sin(x)
    #
    # plt.plot(x,y,color='r',linestyle='-.',label='ss')    #color设置颜色,label为图例设置标签值
    # plt.plot(x,y1,linewidth=3,markerfacecolor='g')     #linewith设置线宽
    #
    # plt.title("function $\sin$ and $\cos$")   #添加标题
    # #设置坐标轴范围
    # plt.xlim(-3.0,3.0)
    # plt.ylim(-1.0,1.0)
    #
    # #format ticks at specific values设置坐标轴显示
    # plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],
    #            [r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])
    # plt.yticks([-1,0,+1],[r'$-1$',r'$0$',r'$+1$'])
    # print plt.axis()
    # plt.show()



    #使用date模块######################################################################
    # fig=plt.figure()
    #
    # #set some daterange
    # start=datetime.datetime(2013,01,01)
    # stop=datetime.datetime(2013,12,31)
    # delta=datetime.timedelta(days=1)
    #
    # #convert dates for matplotlib
    # dates=matplotlib.dates.drange(start,stop,delta)
    #
    # #generate some random values
    # values=np.random.rand(len(dates))
    #
    # ax=gca()
    # ax.plot_date(dates,values,color='r',linestyle='-',marker='',linewidth=0.5)
    # date_format=matplotlib.dates.DateFormatter('%Y-%m-%d')
    # ax.xaxis.set_major_formatter(date_format)
    # fig.autofmt_xdate()
    # show()



    # #添加图例和注释###################################################################
    # #generate different normal distributions
    # x1=np.random.normal(30,3,100)
    # x2=np.random.normal(20,2,100)
    # x3=np.random.normal(10,3,100)
    #
    # #plot them
    # plt.plot(x1,label='plot')
    # plt.plot(x2,label='2nd plot')
    # plt.plot(x3,label='last plot')
    #
    # #generate a legend box
    # plt.legend(bbox_to_anchor=(0.,1.02,1.,.102),loc=3,ncol=3,mode='expand',borderaxespad=0.)  #根据label添加图例
    #
    # #annotate an important value
    # plt.annotate('important value',(55,20),xycoords='data',xytext=(5,38),
    #              arrowprops=dict(arrowstyle='->'))
    #
    # plt.show()


    #绘制直方图########################################################################
    # mu=100
    # sigma=15
    # x=np.random.normal(mu,sigma,10000)
    #
    # ax=plt.gca()
    #
    # #the histogram of the data      bin为直方图直条的数量
    # ax.hist(x,bins=35,color='r')
    # ax.set_xlabel('Values')        #设置x轴label
    # ax.set_ylabel('Frequency')     #设置y轴label
    # ax.set_title(r'$\mathrm{Histogram:}\ \mu=%d,\ \sigma=%d$' %(mu,sigma)) #添加标题
    # show()



    #绘制饼图###########################################################################
    # figure(1,figsize=(6,6))
    # ax=axes([0.1,0.1,0.8,0.8])
    # labels='Spring','Summer','Autumn','Winter'
    # x=[15,30,45,10]
    # explode=(0.1,0.1,0.1,0.1)
    # pie(x,explode=explode,labels=labels)
    # title('Rainy days by season')
    # show()


    #绘制带填充区域的图表##############################################################
    # x=np.arange(0.0,2,0.01)
    # y1=np.sin(2*np.pi*x)
    # y2=1.2*np.sin(4*np.pi*x)
    #
    # fig=figure()
    # ax=gca()
    #
    # ax.plot(x,y1,x,y2,color='black')
    # ax.fill_between(x,y1,y2,where=y2>y1,facecolor='darkblue',interpolate=True)
    # ax.fill_between(x,y1,y2,where=y2<y1,facecolor='deeppink',interpolate=True)
    # ax.set_title('filled between')
    # show()


    #绘制带彩色标记的散点图##############################################################
    x=np.random.randn(1000)
    y1=np.random.randn(len(x))
    y2=1.2+np.exp(x)

    ax1=plt.subplot(121)
    plt.scatter(x,y1,color='indigo',alpha=0.3,edgecolors='white',label='no correlation')
    plt.xlabel('no correlation')
    plt.grid(True)
    plt.legend()

    ax2=plt.subplot(122,sharey=ax1,sharex=ax1)
    plt.scatter(x,y2,color='green',alpha=0.3,edgecolor='grey',label='correl')
    plt.xlabel('strong correlation')
    plt.grid(True)
    plt.legend()
    plt.show()


def super_graph():
    data=np.random.randn(70)
    fontsize=18
    plt.plot(data,color='r',linewidth=0.5)
    title='this is figure title'
    x_label='this is x axis label'
    y_label='this is y axis label'

    title_text_obj=plt.title(title,fontsize=fontsize,
                             verticalalignment='bottom')

    title_text_obj.set_path_effects([patheffects.withSimplePatchShadow()])  #为标题设置阴影


    show()

if __name__ == '__main__':
    super_graph()
