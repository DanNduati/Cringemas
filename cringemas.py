import config
from send_sms import AtSms

#create an AT sms object
at_sms = AtSms(config.username,config.api_key,config.short_code)

recepients = ["+254723060846"]
message = "Hello there!"

def main():
    at_sms.send(recepients,message)

if __name__ == "__main__":
    main()