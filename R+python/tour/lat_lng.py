#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import json
import torndb

reload(sys)
sys.setdefaultencoding("utf-8")


def mysql_connect():
    mysql = {
        "host": "192.168.0.100",
        "port": "3306",
        "database": "tour",
        "password": "123456",
        "user": "root",
        "charset":"utf8"
    }

    db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                           user=mysql.get('user'),
                           password=mysql.get('password'), charset=mysql.get('charset'))
    return db


def load_data():
    db=mysql_connect()
    sql = r"""insert into scenic_spot_location (scenic_spot_id,longitude,demension) values (%s, %s, %s)"""
    with open('lat_lng_area','r') as fr:
        lines=fr.readlines()
        for line in lines:
            lat_lng_dict=json.loads(line.strip())
            try:
                scenic_spot_id=get_scenic_id(lat_lng_dict.get('area'))
            except:
                # print lat_lng_dict.get('area'),'failure to get id'
                continue
            longitude=lat_lng_dict.get('lng')
            demension=lat_lng_dict.get('lat')
            try:
                r = db.insert(sql,scenic_spot_id,longitude,demension)
                # print 'ok'
            except Exception as e:
                print lat_lng_dict.get('area'),'failure to save to mysql'
                continue


def get_scenic_id(name):
    db=mysql_connect()
    select_sql='SELECT id FROM scenic_spot_desc WHERE scenic_spot_name=\''+name+'\';'
    res=db.query(select_sql)
    try:
        res_id=res[0].get('id')
    except IndexError as e:
        print name
    return res_id

def spot_desc_to_sql():
    desc_dict={}
    db=mysql_connect()
    with open('D://gitcode/mypython/R+python/word_cloud/desc','r') as fr:
        lines=fr.readlines()
        for line in lines:
            spot_name=json.loads(line.strip()).get('name')
            if spot_name in desc_dict:
                continue
            else:
                desc=json.loads(line.strip()).get('description')
                desc_dict.update({spot_name:desc})
                # update_sql = '''UPDATE scenic_spot_desc SET text="%s" WHERE scenic_spot_name="%s";''' % (desc,spot_name)
                # try:
                #     db.execute(update_sql)
                #     print 'seccess',spot_name
                # except:
                #     print ' fail to update',spot_name
    # for k,v in desc_dict.items():
    #     print k,v
    # # print desc_dict.get(u'八达岭国家森林公园')
    return desc_dict

def desc_failure():
    db=mysql_connect()
    desc_dict=spot_desc_to_sql()
    with open('failure_desc','r') as fr:
        lines=fr.readlines()
        for line in lines:
            spot_name=line.strip()
            desc=desc_dict.get(line.strip().decode('utf-8'))
            print spot_name+'\x01'+desc
            # update_sql = 'UPDATE scenic_spot_desc SET text=\''+desc+'\' WHERE scenic_spot_name=\''+spot_name+'\';'
            # try:
            #     db.execute(update_sql)
            # except:
            #     print spot_name



if __name__ == '__main__':
    # load_data()
    # spot_desc_to_sql()
    desc_failure()
