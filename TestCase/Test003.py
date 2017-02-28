# -*- coding: utf-8 -*-
import sys
import os
import nose
from nose.tools import assert_not_equal, assert_equal
from nose.plugins.plugintest import run_buffered as run  
from htmloutput.htmloutput import HtmlOutput 

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from Config.EB_API_Config import *
from Common.RoomType import *

class Test003():
    def Setup(self):
        print "Test Start"

    def Test003(self):
        self.CaseNumber="Test003"
        RoomTypeName   =GetNumber(8)
        RoomNumber     =GetNumber(10)
        NewRoomTypeName=GetNumber(9)
        NewRoomNumber  =GetNumber(7)
#1新增房型1和新增房间1，Pass
        RoomType=Add_RoomType(CaseNumber=self.CaseNumber,
                              url=RoomType_API_url,
                              RoomTypeName=RoomTypeName,
                              RoomNumber=RoomNumber,
                              weekdayPrice='300')
        Result = RoomType['Result']
        assert_equal(Result,True,msg="businessCode and resultCode is Error")

#2检查新增的房型1和房间1状态 ，Pass       
        Status=RoomType_Status(CaseNumber=self.CaseNumber,
                               url=RoomType_Status_url,
                        RoomTypeId=RoomType['RoomTypeId'])

        Result = Status['Result']
        assert_equal(Result,True,msg="businessCode and resultCode is Error")

#3在房型1下新增房间2，Pass        
        RoomType1=Add_RoomType(CaseNumber=self.CaseNumber,
                              url=RoomType_API_url,
                              RoomTypeName=RoomType['RoomTypeName'],
                              RoomNumber=NewRoomNumber,
                              weekdayPrice='300')
        Result = RoomType1['Result']
        assert_equal(Result,True,msg="businessCode and resultCode is Error")

#4新增已存在的房型和房间，Failed        
        RoomType2=Add_RoomType(CaseNumber=self.CaseNumber,
                              url=RoomType_API_url,
                              RoomTypeName=RoomType['RoomTypeName'],
                              RoomNumber=RoomType['RoomNumber'],
                              weekdayPrice='300')
        Result = RoomType2['Result']
        assert_equal(Result,False,msg="businessCode and resultCode is Error")
        
#5删除房型1，Pass        
        Del=Del_RoomType(CaseNumber=self.CaseNumber,
                     url=RoomType_API_url, 
                     RoomTypeId=RoomType['RoomTypeId'])
         
        Result = Del['Result']
        assert_equal(Result,True,msg="businessCode and resultCode is Error")

#6新增房型1和房间1，Pass        
        RoomType3=Add_RoomType(CaseNumber=self.CaseNumber,
                              url=RoomType_API_url,
                              RoomTypeName=RoomType['RoomTypeName'],
                              RoomNumber=RoomType['RoomNumber'],
                              weekdayPrice='300')
        Result = RoomType3['Result']
        assert_equal(Result,True,msg="businessCode and resultCode is Error")

#7搜索新增的房型1和房间1，Pass                        
        Serach=Search_RoomType(CaseNumber=self.CaseNumber,
                               url=Search_RoomType_url,
                               RoomTypeName=RoomType3['RoomTypeName'],
                               RoomNumber=RoomType3['RoomNumber'],
                               RoomTypeId=RoomType3['RoomTypeId'])
        Result = Serach['Result']
        assert_equal(Result,True,msg="businessCode and resultCode is Error")
                
    def CleanUp(self):
        print "Test End"