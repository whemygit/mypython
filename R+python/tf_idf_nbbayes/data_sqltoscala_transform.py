#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import sys
import re
import time
import json
import torndb
import jieba
reload(sys)
sys.setdefaultencoding("utf-8")

def mysql_connect():
    mysql_par = {'ip': "192.168.0.202:3306",
                 'port': '3306',
                 'database': 'spider',
                 'user': 'suqi',
                 'password': '123456',
                 'charset':'utf8'}

    # mysql_par={'ip':"119.57.93.42",
    #            'port':'3306',
    #            'database':'spider',
    #            'user':'bigdata',
    #            'password':'zhongguangzhangshi'}


    db = torndb.Connection(host=mysql_par.get('ip'),
                           database=mysql_par.get('database'),
                           user=mysql_par.get('user'),
                           password=mysql_par.get('password'),
                           charset=mysql_par.get('charset'),
                           )
    return db

def news_cut_outstop(news_text):
    stopwd=[line.strip().decode('utf-8') for line in open('D:/gitcode/mypython/R+python/my_news_classify/stopw.txt','r').readlines()]
    news_text=news_text.replace('\t', '').replace('\n', '').replace(' ', '').replace('，', '')
    seg_list=jieba.cut(news_text,cut_all=False)
    seg_list_outstop=[w for w in seg_list if w not in stopwd]
    return seg_list_outstop

def read_write_data():
    db=mysql_connect()
    select_sql='''SELECT newsid,text FROM _news_data_copy WHERE classify_tag=3;'''
    res=db.query(select_sql)
    with open('predict_data','w') as fw:
        for i in res:
            #print i.get("text")
            newsid=i.get("newsid")
            content = re.sub('<.*?>','',i.get("text"))
            text = re.sub(r'&#13;', '', content).strip()
            line_seg=news_cut_outstop(text)
            line_seg=' '.join(line_seg)
            fw.write(str(newsid) + ',' + line_seg + '\n')


def read_and_update():
    '''
    根据读入的scala预测结果文件，对mysql数据库操作
    :return:
    '''
    with open('part-00000','r') as fr:
        lines=fr.readlines()
        db = mysql_connect()
        for line in lines:
            read_list=eval(line)
            newsid=int(read_list[0])
            tag=int(read_list[1])
            print newsid,tag
            update_sql='''UPDATE _news_data_copy SET classify_tag=%s WHERE newsid=%s;''' %(tag,newsid)
            db.execute(update_sql)
            break


if __name__ == '__main__':
    read_and_update()