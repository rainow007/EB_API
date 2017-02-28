#coding=utf-8
import sys
import os
import nose
from nose.tools import assert_equal
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from Config.EB_API_Config import *
from Common.RoomType import *
import requests


# 办理预订、入住
def Order_Check_In(**self):
    payload = {
    "OccupationChangedList": [],
    "BillItemChangedList": [],
    "CustomerChangedList": [],
    "Data":
    {
    "Action": self['Action'],
    "BillItems": [
        {
            "IsDeposit": False,
            "Amount": 100,
            "CreditTypeValue": self['CreditTypeValue'],
            "CreditTypeName": self['CreditTypeName'],
            "DebitTypeValue": "D1000",
            "DebitTypeName": "房费"
        }
    ],
    "Channel": {
        "k": self['Channel_K'],
        "v": self['Channel_V']
    },
    "CheckinType": "Normal",
    "HasGuaranty": False,
    "IsCheckout": False,
    "Liaison": {
        "Address": "",
        "Folk": "",
        "Gender": "0",
        "Mobile": "",
        "Name": "shenyong",
        "Point": 0.0,
        "arrowStatus": False
    },
    "OccupationsInfo": [
        {
            "EndDateTime":"%s"%tomorrow,
            "RoomFee": [
                {
                    "ActualPrice": 300.0,
                    "Date": "%s"%today,
                    "ExternalPrice": 0.0,
                    "IsExternalPrice": False,
                    "OrignMarketPrice": 300.0
                }
            ],
            "RoomNumber": self['RoomNumber'],
            "RoomType": {
                "k": self['RoomTypeId'],
                "v": "3"
            },
            "StartDateTime": "%s"%today
        }
    ],
    "Remark": ""
    }
}
    r = requests.request('POST',
                              self['url'], 
                              headers=Headers ,
                              data=json.dumps(payload))
        
    Order_Check_In_data = json.loads(r.text)
    businessCode=CommonMoudle(Order_Check_In_data['businessCode'] ,200)
    resultCode=CommonMoudle(Order_Check_In_data['resultCode'] ,200) 

    if businessCode & resultCode ==True:
        OrderId = Order_Check_In_data['data']['OrderId']
        Order_Status = Order_Check_In_data['data']['OccupationsInfo'][0]['Status']['v']
        Check_In_Details = {
        	                    'OrderId':OrderId,
        	                    'Order_Status':Order_Status,
        	                    'Result':True}
        print Check_In_Details
        return Check_In_Details
    else:
        Check_In_Details = {'Result',False}
        print Check_In_Details
        return Check_In_Details


if __name__ == "__main__":
    Available=Available_Room(url=Available_Room_url,
                    StartDate=today,
                    EndDate=tomorrow)

    Result = Available['Result']

    assert_equal(Result,True,msg="businessCode and resultCode is Error")

    Order_Check_In(Action = 0,
    CreditTypeValue = CreditTypeValue['微信'],
    CreditTypeName = '微信',
    Channel_K = Channel_K['去哪儿'],
    Channel_V = '去哪儿',
    RoomNumber = Available['RoomNumber'],
    RoomTypeId = Available['RoomTypeId'],
    url = Check_In_url)

