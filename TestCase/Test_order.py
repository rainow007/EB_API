#conding=utf-8
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

class Test_order():
	def setUp(self):
		print "Test start"

	def Test(self):
		self.CaseNumber = "Test_order"
		Booking_Details = Order_Booking(
			CaseNumber = sefl.CaseNumber,
			Action = 0,
			url = Check_In_url,
			CreditTypeValue = CreditTypeValue['现金'],
			CreditTypeName = '现金',
			Channel_K = Channel_K['酒店前台'],
			Channel_V = '酒店前台',
			RoomNumber=RoomType['RoomNumber'],
            RoomTypeId=RoomType['RoomTypeId']
			)
		Result = Booking_Details['Result']

		assert_equal[Result,True]