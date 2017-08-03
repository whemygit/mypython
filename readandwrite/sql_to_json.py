#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import torndb
import json
import datetime

reload(sys)
sys.setdefaultencoding("utf-8")

def mysql_connect():
    # mysql_par={'ip':"192.168.0.202",
    #            'port':'3306',
    #            'database':'spider',
    #            'user':'root',
    #            'password':'neiwang-zhongguangzhangshi'}

    mysql_par = {'ip': "192.168.1.8",
                 'port': '3306',
                 'database': 'cityparlor',
                 'user': 'bigdata',
                 'password': 'zhongguangzhangshi'}


    db=torndb.Connection(host=mysql_par['ip'],
                         database=mysql_par['database'],
                         user=mysql_par['user'],
                         password=mysql_par['password'])
    return db


def tab_json(tab_name):
    db=mysql_connect()
    select_sql='''select * from %s''' %tab_name
    print select_sql
    ouput_file='/home/database_to_json/result/'+tab_name
    # ouput_file = 'result/' + tab_name
    print ouput_file
    res=db.query(select_sql)
    with open(ouput_file,'w') as fw:
        for r in res:
            # print r
            # break
            if isinstance(r.get('create_date'), datetime.date):
                r['create_date']=r.get('create_date').strftime("%Y-%m-%d")
            if isinstance(r.get('update_date'), datetime.date):
                r['update_date']=r.get('update_date').strftime("%Y-%m-%d")
            if isinstance(r.get('release_date'), datetime.date):
                r['release_date'] = r.get('release_date').strftime("%Y-%m-%d")
            res_json=json.dumps(r)
            fw.write(res_json+'\n')
    db.close()



if __name__ == '__main__':
    tab_names = ['t_town_news','t_channel_news','t_collect_news']
    # tab_names = ['t_town_news']
    for tab_name in tab_names:
        tab_json(tab_name)