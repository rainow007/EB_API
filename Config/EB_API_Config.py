# -*- coding: utf-8 -*-
import requests
import json
import random
import logging
import datetime
import time
import MySQLdb
import MySQLdb.cursors
import string
from random import choice
from Common.PO_Search import *

#获取随机函数
def GetNumber(length=8, chars=string.letters+string.digits):
    return ''.join([choice(chars) for i in range(length)])

#bussnesscode和resultcode的判断
def CommonMoudle(Path, data):
    if Path == data:
        return True
    else:
        return False

Room ={'RoomTypeName':random.getrandbits(20),
       'RoomNumber':random.getrandbits(20),
       'NewRoomTypeName':random.getrandbits(30)}

Headers={'Content-Type':'application/json',
         'ownerid':'434265567985665',
         'orgid':'434265567985667'}

#支付方式
CreditTypeValue = {'现金':'C9110','微信':'C9140','支付宝':'C9310','银行卡':'C9120','其它':'C9900'}
#CreditTypeName = {'现金','微信','支付宝','银行卡','其它'}

#订单渠道
Channel_K = {'酒店前台':'Hotel','美团':'MeiTuanEBK','携程':'CTRIP','艺龙':'ELONG','去哪儿':'QUNAR','阿里旅行':'TAOBAO'}
# Channel_V = {'酒店前台','美团','携程','艺龙','去哪儿','阿里旅行'}

conn= MySQLdb.connect(
        host='192.168.9.24',
        port = 3306,
        user='root',
        passwd='p@ssw0rd',
        db ='iPms',
        charset='utf8',
        cursorclass = MySQLdb.cursors.DictCursor
        )

conn1= MySQLdb.connect(
        host='192.168.9.24',
        port = 3306,
        user='root',
        passwd='p@ssw0rd',
        db ='iPmsBiz',
        charset='utf8',
        cursorclass = MySQLdb.cursors.DictCursor
        )

FileName = time.strftime('%Y%m%d_%H:%M:%S',time.localtime(time.time()))
today = datetime.date.today()
yesterday= today - datetime.timedelta(days=15)
tomorrow=today+datetime.timedelta(days=15)

#Server='http://192.168.32.179'

Server='http://192.168.32.179'
# Server='http://testwww.51pms.net:'

Port=''


RoomType_API          ='/api/rooms/RoomType/'

Search_RoomType_API   ='/api/rooms/RoomTypes/'

RoomType_Status_API   ='/api/rooms/CanDeleteRoomType/'

PO_Search_API         ='/api/GuestFolios/eb/combine?OwnerIds=%s'%Headers['ownerid']

Check_In_API          ='/api/ordercheckin/pos'

Check_Out_API          ='/api/ordercheckin/Checkout/'

Register_API            ='/meituan/eb/register'

Available_Room_API          ='/api/ordercheckin/BasicData/'



RoomType_API_url     = Server+Port+RoomType_API

RoomType_Status_url  = Server+Port+RoomType_Status_API

Search_RoomType_url  = Server+Port+Search_RoomType_API 

PO_Search_url        = Server+Port+PO_Search_API 

Check_In_url         = Server+Port+Check_In_API

Check_Out_url         = Server+Port+Check_Out_API

Register_API_url      = Server+Port+Register_API

Available_Room_url    = Server+Port+Available_Room_API




