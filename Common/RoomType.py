from Config.EB_API_Config import *
from nose.config import flag

def CommonMoudle(Path,data):
    if Path==data:
        return True
    else:
        return False

#def Modify_RoomType(url,RoomTypeName,RoomTypeId,weekdayPrice,RoomNumber1,RoomID,IsActive1):
def Modify_RoomType(**self):
        payload = {
                    "Id": self['RoomTypeId'],
                    "RoomTypeName": self['RoomTypeName'],
                    "weekdayPrice": self['weekdayPrice'],
                    "IsActive": True,
                    "Rooms": [
            {
                "Id":self['RoomID'],
                "RoomNumber": self['RoomNumber1'],
                "IsActive": self['IsActive1']
            }
        ]
        }
                   
        r = requests.request('PUT', self['url'], headers=Headers ,data=json.dumps(payload))

        Modify_RoomType_data = json.loads(r.text)
        businessCode=CommonMoudle(Modify_RoomType_data['businessCode'] ,200)
        resultCode=CommonMoudle(Modify_RoomType_data['resultCode'] ,200)
        NewRoomTypeName=Modify_RoomType_data['data']['RoomTypeName']
        NewIsActive=Modify_RoomType_data['data']['Rooms'][0]['IsActive']
        weekdayPrice=Modify_RoomType_data['data']['weekdayPrice']        
        RoomNumber=Modify_RoomType_data['data']['Rooms'][0]['RoomNumber']
        RoomTypeId=Modify_RoomType_data['data']['Rooms'][0]['RoomTypeId']   
         
        if businessCode & resultCode ==True:
            if weekdayPrice==999 and NewRoomTypeName==str(RoomTypeName) and NewIsActive==False:
                print "Modify_RoomType is Pass. Date:%s"%today
                return True
            else:
                print "Modify_RoomType is Failed. Date:%s"%today
                return False
        else:
            print "Modify_RoomType is Failed. Date:%s"%today
            return False            

def Del_RoomType(url,RoomTypeID):
    r = requests.request('DELETE', url+RoomTypeID, headers=Headers)
    Del_RoomType_data = json.loads(r.text)
    businessCode=CommonMoudle(Del_RoomType_data['businessCode'] ,200)
    resultCode=CommonMoudle(Del_RoomType_data['resultCode'] ,200) 
    
    
    if businessCode & resultCode ==True:
        print "Del_RoomType is Pass. Date:%s"%today
        return True
    else:
        print "Del_RoomType is Failed. Date:%s"%today
        return False        

def Add_RoomType(**self):
        payload = {
                   "RoomTypeName": self['RoomTypeName'],
                   "weekdayPrice": self['weekdayPrice'],
                   "IsActive": True,
                   "Rooms": [
                    {
                    "RoomNumber": self['RoomNumber'],
                    "IsActive": True
                    }
                             ]


                             }
        r = requests.request('POST',
                              self['url'], 
                              headers=Headers ,
                              data=json.dumps(payload))

        Add_RoomType_data = json.loads(r.text)
        businessCode=CommonMoudle(Add_RoomType_data['businessCode'] ,200)
        resultCode=CommonMoudle(Add_RoomType_data['resultCode'] ,200) 
        Message=Add_RoomType_data['Message']
        
        if businessCode & resultCode ==True:
            print "Add_RoomType is Pass. Message:%s Date:%s"%(Message,today)  
            RoomTypeName=Add_RoomType_data['data']['RoomTypeName']
            RoomNumber=Add_RoomType_data['data']['Rooms'][0]['RoomNumber']
            RoomTypeId=Add_RoomType_data['data']['Rooms'][0]['RoomTypeId']
            RoomID=Add_RoomType_data['data']['Rooms'][0]['Id']
            Add_RoomType={'RoomTypeName':RoomTypeName,
               'RoomNumber':RoomNumber,
               'RoomTypeId':RoomTypeId,
               'RoomID':RoomID,
               'Result':True}
            print Add_RoomType['RoomTypeName']
            return dict(Add_RoomType)

        else:
            print "Add_RoomType is Failed. Message:%s Date:%s"%(Message,today)
            return False

def Search_RoomType(url,RoomTypeName=None,RoomNumber=None,RoomTypeId=None):
    r = requests.request('GET', url, headers=Headers)
    All_RoomType_data = json.loads(r.text)
        
    if  RoomTypeName is None and RoomNumber is None:
        businessCode=CommonMoudle(All_RoomType_data['businessCode'] ,200)
        resultCode=CommonMoudle(All_RoomType_data['resultCode'] ,200)
        if businessCode==True and resultCode==True:
            print "Search_RoomType is Pass. Date:%s"%today
            return True
        else:
            print "Search_RoomType is Failed!!. Date:%s"%today
            return False                               

    else:
        flag=True        
        for v in All_RoomType_data['data']:
            i=v
            if i['RoomTypeName']==RoomTypeName:
                for v in i['Rooms']:
                    if v['RoomNumber']==RoomNumber:
                        print "Add_RoomType is Pass In Search_RoomType!. Date:%s"%today
                        flag=False
                    else:
                        print "Add_RoomType is Failed In Search_RoomType!. Date:%s"%today 
                        continue                 
    if flag:
        print "Add_RoomType is Failed In Search_RoomType!!. Date:%s"%today
        return False
        
    sql=("SELECT * FROM iPms.RoomType where id = '%s' and IsVirtual = 1;")%RoomTypeId
    curs = conn.cursor()
    RoomTypeTotal=curs.execute(sql)
    conn.close()
    
    if RoomTypeTotal==1:
        print "Data:RoomType TotalAmount is Pass"
        return True
    else:
        print "Data:RoomType TotalAmount is Failed"
        return False
        
def RoomType_Status(**self):
    if self['RoomTypeId']==None:
        print "RooMTypeID is None Date:%s"%today
        return False
    else:
        r = requests.request('GET', self['url']+self['RoomTypeId'], headers=Headers)
        RoomType_Status_data = json.loads(r.text)

        Status=CommonMoudle(RoomType_Status_data['data'] ,True)
        if Status==True:
            print "RoomType_Status is True. Date:%s"%today
            return True
        elif Status==False:
            print "RoomType_Status is False. Date:%s"%today
            return True
        else:
            print "RoomType_Status is failed. Date:%s"%today
            return False
        
                                   
if __name__ == "__main__":
    Add_RoomType=Add_RoomType(url=RoomType_API_url,RoomTypeName=Room['RoomTypeName'],RoomNumber=Room['RoomNumber'],weekdayPrice='300')
    print Add_RoomType['RoomTypeId']

     
    RoomType_Status(url=RoomType_Status_url,
                    RoomTypeId=Add_RoomType['RoomTypeId'])

#def Modify_RoomType(url,RoomTypeName,RoomTypeId,weekdayPrice,RoomNumber1,RoomID,IsActive1):
    
#     Modify_RoomType(
#                     RoomType_API_url,
#                     Room['NewRoomTypeName'],
#                     Add_RoomType['RoomTypeId'],
#                     999,
#                     Add_RoomType['RoomNumber'],
#                     Add_RoomType['RoomID'],
#                     False)
#       
#     Del_RoomType(RoomType_API_url, Add_RoomType['RoomTypeId']) 
#         
#     RoomType_Status(RoomType_Status_url,Add_RoomType['RoomTypeId'])
#     
#     Search_RoomType(Search_RoomType_url,Add_RoomType['RoomTypeName'],Add_RoomType['RoomNumber'],Add_RoomType['RoomTypeId'])





    
    
    
    
    