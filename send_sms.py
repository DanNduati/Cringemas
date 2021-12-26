import africastalking as at
from twilio.rest import Client
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
    def __init__(self,account_sid:str,auth_token:str):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.client = Client(account_sid,auth_token)
    def send(self,sender:str,recepient:str,msg:str):
        message = self.client.messages.create(
            body = msg,
            from_ = sender,
            to=recepient
        )
        print(message.sid)