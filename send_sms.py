import africastalking as at

#africas talking
class AtSms:
    def __init__(self,username:str,api_key:str,sender:str):
        self.username = username
        self.api_key = api_key
        self.sender = sender
        #initialize the sdk
        at.initialize(self.username,self.api_key)
        #get sms service
        self.sms = at.SMS
    
    def send(self,recepients:list,message:str):
        self.recepients = recepients
        self.message = message
        try:
            response = self.sms.send(self.message,self.recepients,self.sender)
            print(response)
        except Exception as e:
            print(e)
#twilio
class TwilioSms():
    pass