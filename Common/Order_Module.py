# -*- coding: utf-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from Config.EB_API_Config import *
import requests


# 办理预订、入住
def Order_Booking(**self):
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
            "StartDateTime": "%s"%yesterday
        }
    ],
    "Remark": ""
    }
}
    r = requests.request('POST',
                              self['url'], 
                              headers=Headers ,
                              data=json.dumps(payload))
        
    Order_Booking_data = json.loads(r.text)
    businessCode=CommonMoudle(Order_Booking_data['businessCode'] ,200)
    resultCode=CommonMoudle(Order_Booking_data['resultCode'] ,200) 

    if businessCode & resultCode ==True:
        OrderId = Order_Booking_data['data']['OrderId']
        Order_Status = Order_Booking_data['OccupationsInfo'][2]['Status']['v']
        Booking_Details = {
        	                    'OrderId':OrderId,
        	                    'Order_Status':Order_Status,
        	                    'Result':True}
        print "ok"
        return Booking_Details
    else:
        Booking_Details = {'Result',False}
        print "Error"
        return Booking_Details


if __name__ == "__main__":
    Order_Booking(Action = 0,
    CreditTypeValue = 'C9110',
    CreditTypeName = '现金',
    Channel_K = 'Hotel',
    Channel_V = '酒店前台',
    RoomNumber = 'LDEVKM',
    RoomTypeId = '5FAIUJ45JF',
    url = Check_In_url)

