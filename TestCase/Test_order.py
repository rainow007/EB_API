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
from Common.Order_Module import *
from Common.RoomType import *


class Test_order():
	def setUp(self):
		print "Test start"

	def Test(self):
		self.CaseNumber = "Test_order"
		Available = Available_Room(url=Available_Room_url,
                    StartDate=today,
                    EndDate=tomorrow)

		Result = Available['Result']
		assert_equal(Result,True,msg = "businessCode and resultCode is Error")

		Check_In = Order_Check_In(Action = 0,
		CreditTypeValue = CreditTypeValue['微信'],
    	CreditTypeName = '微信',
    	Channel_K = Channel_K['去哪儿'],
    	Channel_V = '去哪儿',
    	RoomNumber = Available['RoomNumber'],
    	RoomTypeId = Available['RoomTypeId'],
    	url = Check_In_url )

		Result = Check_In['Result']
		Order_Status = Check_In['Order_Status']
		assert_equal(Result,True,msg = "businessCode and resultCode is Error")
		assert_equal(Order_Status,u'\u5df2\u9884\u8ba2',msg = "businessCode and resultCode is Error")
