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

class Test001():
    def setUp(self):
        print "Test Start"



    def Test001(self):
        self.CaseNumber="Test001"
        RoomTypeName=GetNumber(8)
        RoomNumber=GetNumber(10)
        NewRoomTypeName=GetNumber(9)
  
        RoomType=Add_RoomType(CaseNumber=self.CaseNumber,
                              url=RoomType_API_url,
                              RoomTypeName=RoomTypeName,
                              RoomNumber=RoomNumber,
                              weekdayPrice='300')

        Result = RoomType['Result']

        assert_equal(Result,True,msg="businessCode and resultCode is Error")
               
        Status=RoomType_Status(CaseNumber=self.CaseNumber,
                               url=RoomType_Status_url,
                        RoomTypeId=RoomType['RoomTypeId'])

        
        Result = Status['Result']
        assert_equal(Result,True,msg="businessCode and resultCode is Error")
        
        Modify=Modify_RoomType(CaseNumber=self.CaseNumber,
                               url=RoomType_API_url,
                        RoomTypeName=Room['NewRoomTypeName'],
                        RoomTypeId=RoomType['RoomTypeId'],
                        weekdayPrice=999,
                        RoomNumber=RoomType['RoomNumber'],
                        RoomID=RoomType['RoomID'],
                        IsActive=False)
        
        Result = Modify['Result']
        weekdayPrice = Modify['weekdayPrice']
        assert_equal(Result,True)
        assert_equal(weekdayPrice,999,msg="weekdayPrice is Error")
        
        Del=Del_RoomType(CaseNumber=self.CaseNumber,
                     url=RoomType_API_url, 
                     RoomTypeId=RoomType['RoomTypeId'])
         
        Result = Del['Result']
        assert_equal(Result,True,msg="businessCode and resultCode is Error")
        
        Status=RoomType_Status(CaseNumber=self.CaseNumber,
                               url=RoomType_Status_url,
                        RoomTypeId=RoomType['RoomTypeId'])

        
        Result = Status['Result']
        assert_equal(Result,False,msg="businessCode and resultCode is Error")
        
        Serach=Search_RoomType(CaseNumber=self.CaseNumber,
                               url=Search_RoomType_url,
                               RoomTypeName=RoomType['RoomTypeName'],
                               RoomNumber=RoomType['RoomNumber'],
                               RoomTypeId=RoomType['RoomTypeId'])

        Result = Serach['Result']
        assert_equal(Result,False,msg="businessCode and resultCode is Error")
                
    def tearDown(self):
        print "Test End"
#         path= os.path.dirname(__file__)  
#         print path
#         outfile = os.path.join(path, "result.html")  
#         print outfile
#         run(argv=['nosetests', '-v','--with-html-output','--html-out-file=result.html'],plugins=[HtmlOutput()])


    
    