
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

class Test002():
    # def __init__(self, CaseNumber):
    #     self.CaseNumber = CaseNumber

    def setUp(self):
        print "Test Start"



    def Test(self):
        self.CaseNumber="Test002"
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
        
        Del=Del_RoomType(CaseNumber=self.CaseNumber,
                     url=RoomType_API_url, 
                     RoomTypeId=RoomType['RoomTypeId'])
         
        Result = Del['Result']
        assert_equal(Result,True,msg="businessCode and resultCode is Error")
        
        Status=RoomType_Status(CaseNumber=self.CaseNumber,
                               url=RoomType_Status_url,
                        RoomTypeId=RoomType['RoomTypeId'])       
        Result = Status['Result']
        assert_equal(Result,False,)
        
        Modify=Modify_RoomType(CaseNumber=self.CaseNumber,
                               url=RoomType_API_url,
                        RoomTypeName=Room['NewRoomTypeName'],
                        RoomTypeId=RoomType['RoomTypeId'],
                        weekdayPrice=999,
                        RoomNumber=RoomType['RoomNumber'],
                        RoomID=RoomType['RoomID'],
                        IsActive=False)        
        Result = Modify['Result']
        # if (Result != False):
        #     return Result
        assert_equal(Result,False)
                
        Serach=Search_RoomType(CaseNumber=self.CaseNumber,
                               url=Search_RoomType_url,
                               RoomTypeName=RoomType['RoomTypeName'],
                               RoomNumber=RoomType['RoomNumber'],
                               RoomTypeId=RoomType['RoomTypeId'])
        Result = Serach['Result']
        # if (Result != True):
        #     return Result        
        assert_not_equal(Result,True)
                
    def tearDown(self):
        print "Test End"


# if __name__ == "__main__":
#     test = Test002('TCS002')
#     test.Test(CaseNumber='TCS002')