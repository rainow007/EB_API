from Common.RoomType import *

class UseTest():
    def __init__(self, CaseNumber):
        self.CaseNumber = CaseNumber

    def Setup(self):
        print "Test Start"



    def Test(self,CaseNumber):
        RoomTypeName=GetNumber(8)
        RoomNumber=GetNumber(10)
        NewRoomTypeName=GetNumber(9)
  
        RoomType=Add_RoomType(CaseNumber=self.CaseNumber,
                              url=RoomType_API_url,
                              RoomTypeName=RoomTypeName,
                              RoomNumber=RoomNumber,
                              weekdayPrice='300')
        Result = RoomType['Result']
        if (Result != True):
            return Result
        
        Status=RoomType_Status(CaseNumber=self.CaseNumber,
                               url=RoomType_Status_url,
                        RoomTypeId=RoomType['RoomTypeId'])

        Result = Status['Result']
        if (Result != True):
            return Result
        
        RoomType1=Add_RoomType(CaseNumber=self.CaseNumber,
                              url=RoomType_API_url,
                              RoomTypeName=RoomType['RoomTypeName'],
                              RoomNumber=RoomType['RoomNumber'],
                              weekdayPrice='300')
        Result = RoomType1['Result']
        if (Result != False):
            return Result
        
        Del=Del_RoomType(CaseNumber=self.CaseNumber,
                     url=RoomType_API_url, 
                     RoomTypeId=RoomType['RoomTypeId'])
         
        Result = Del['Result']
        if (Result != True):
            return Result
        
        RoomType=Add_RoomType(CaseNumber=self.CaseNumber,
                              url=RoomType_API_url,
                              RoomTypeName=RoomType['RoomTypeName'],
                              RoomNumber=RoomType['RoomNumber'],
                              weekdayPrice='300')
        Result = RoomType['Result']
        if (Result != True):
            return Result        
                        
        Serach=Search_RoomType(CaseNumber=self.CaseNumber,
                               url=Search_RoomType_url,
                               RoomTypeName=RoomType['RoomTypeName'],
                               RoomNumber=RoomType['RoomNumber'],
                               RoomTypeId=RoomType['RoomTypeId'])
        Result = Serach['Result']
        if (Result != True):
            return Result        
                
    def CleanUp(self):
        print "Test End"


if __name__ == "__main__":
    test = UseTest('TCS004')
    test.Test(CaseNumber='TCS004')
    
    