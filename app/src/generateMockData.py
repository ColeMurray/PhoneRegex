# GenerateMockData.py
# Creates a .csv file
# consisting of person, (optional)
# city, and phone number tuples
# ie. John Doe, 555-5555
# ie. John Doe, 555-5555
#
# Numbers can also be improperly
# formatted
# ie. John Doe, 55555555
#

class CustomerInfo:
    def __init__(self,fullName,phoneNum):
        self.fullName = fullName;
        self.phoneNum = phoneNum;

    def __repr__(self):
        return ('Customer: ' + str(self.fullName) + ' ' + str(self.phoneNum))
# end_CustomerInfo

def getArrayOfMockCustomerInfo(customerAmount):
    customerInfoList = []
    for i in range(1,customerAmount):
        customer = CustomerInfo(getRandomFirstName(),getRandomPhoneNumber());
    
        customerInfoList.append(customer);

    return customerInfoList

def getRandomFirstName():
    return "Cole"

def getRandomPhoneNumber():
    return "555-5555"

infoList = getArrayOfMockCustomerInfo(5)
print infoList






# getMockData
# Returns an array of person,phoneNumber
# tuples
#

