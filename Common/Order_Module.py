#coding=utf-8
import random
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
        
        T=r.elapsed.microseconds/1000

        Order_Booking_data = json.loads(r.text)
        businessCode=CommonMoudle(Order_Booking_data['businessCode'] ,200)
        resultCode=CommonMoudle(Order_Booking_data['resultCode'] ,200) 

        if businessCode & resultCode ==True and T<300:
        	OrderId = Order_Booking_data['data']['OrderId']
        	Order_Status = Order_Booking_data['OccupationsInfo'][2]['Status']['v']
        	Booking_Details = {
        	                    'OrderId':OrderId,
        	                    'Order_Status':Order_Status,
        	                    'Result':True}
        	return Booking_Details

        else:
        	Booking_Details = {'Result',False}
        	return Booking_Details
            


# 办理入住
# def Order_Check_In(**self):
# 		payload = {
#     "OccupationChangedList": [],
#     "BillItemChangedList": [],
#     "CustomerChangedList": [],
#     "Data":
#     {
#     "Action": "1",
#     "BillItems": [
#         {
#             "IsDeposit": False,
#             "Amount": 100,
#             "CreditTypeValue": "C9140",
#             "CreditTypeName": "微信",
#             "DebitTypeValue": "D1000",
#             "DebitTypeName": "房费"
#         }
#     ],
#     "Channel": {
#         "k": "Hotel",
#         "v": "酒店前台"
#     },
#     "CheckinType": "Normal",
#     "HasGuaranty": False,
#     "IsCheckout": False,
#     "Liaison": {
#         "Address": "",
#         "Folk": "",
#         "Gender": "0",
#         "Mobile": "",
#         "Name": "wangsheng",
#         "Point": 0.0,
#         "arrowStatus": False
#     },
#     "OccupationsInfo": [
#         {
#             "EndDateTime":"%s"%tomorrow,
#             "RoomFee": [
#                 {
#                     "ActualPrice": 300.0,
#                     "Date": "%s"%today,
#                     "ExternalPrice": 0.0,
#                     "IsExternalPrice": False,
#                     "OrignMarketPrice": 300.0
#                 }
#             ],
#             "RoomNumber": self['RoomNumber'],
#             "RoomType": {
#                 "k": self['RoomTypeId'],
#                 "v": "3"
#             },
#             "StartDateTime": "%s"%yesterday
#         }
#     ],
#     "Remark": ""
#     }
# }

# 		r = requests.request('post',
# 							  self['url'],
# 							  headers = headers,
# 							  data = json.dumps(payload))

# 		Order_Check_In_data = json.dumps(r.text)
# 		businessCode = CommonMoudle(Order_Check_In_data['businessCode'],200)
# 		resultCode = CommonMoudle(Order_Check_In_data['resultCode'],200)

# 		if businessCode & resultCode == True:
# 			OrderId = Order_Booking_data['data']['OrderId']
#         	Order_Status = Order_Booking_data['OccupationsInfo'][2]['Status']['v']
#         	Check_In_Details = {
#         	'OrderId':OrderId,
#         	'Order_Status':Order_Status
#         	}
# 			return Check_In_Details
# 		else:
# 			Check_In_Daily = {'Result',False}
# 			return Check_In_Details
