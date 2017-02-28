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

class Test004():
    def Setup(self):
        print "Test Start"

    def Test004(self):
        self.CaseNumber="Test004"
        RoomTypeName = random.sample(xrange(90000000), 100)
        RoomNumber   = random.sample(xrange(80000000), 100)
  
        RoomType=BatchAdd_RoomType(CaseNumber=self.CaseNumber,
                          url=Search_RoomType_url,
                          RoomTypeName1=RoomTypeName[1],
                          OTARoomTypeName='Test',
                          OTARoomTypeId='Z23582JSC',
                          RoomNumber1_1=RoomNumber[1],
                          RoomNumber1_2=RoomNumber[2],
                          RoomTypeName2=RoomTypeName[2],
                          RoomNumber2_1=RoomNumber[3],
                          RoomNumber2_2=RoomNumber[4],
                          weekdayPrice='300')
        Result = RoomType['Result']
        assert_equal(Result,True,msg="businessCode and resultCode is Error")

        BatchAdd=BatchAdd_RoomType(CaseNumber=self.CaseNumber,
                          url=Search_RoomType_url,
                          RoomTypeName1=RoomTypeName[1],
                          OTARoomTypeName='Test',
                          OTARoomTypeId='Z23582JSC',
                          RoomNumber1_1=RoomNumber[1],
                          RoomNumber1_2=RoomNumber[2],
                          RoomTypeName2=RoomTypeName[2],
                          RoomNumber2_1=RoomNumber[3],
                          RoomNumber2_2=RoomNumber[4],
                          weekdayPrice='300')
        Result = BatchAdd['Result']
        print Result
        assert_equal(Result,False,msg="businessCode and resultCode is Error")
       
                
    def CleanUp(self):
        print "Test End"

    