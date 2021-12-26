import config
from send_sms import AtSms
from send_sms import TwilioSms

#create an AT sms object
at_sms = AtSms(config.username,config.api_key,config.short_code)
twilio_sms = TwilioSms(config.account_sid,config.auth_token)

recepients = ["+254723060846"]
message = "Hello there!"

def main():
    at_sms.send(recepients,message)
    twilio_sms.send(config.sender,recepients[0],message)

if __name__ == "__main__":
    main()