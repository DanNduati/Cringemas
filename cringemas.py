import config
import asyncio
from send_sms import AtSms
from send_sms import TwilioSms
from contacts import gen_dict
from fetch_message import fetch_data

#create an AT and twilio sms object
at_sms = AtSms(config.username,config.api_key,config.short_code)
twilio_sms = TwilioSms(config.account_sid,config.auth_token)

def main():
    contact_data = gen_dict()
    names = list(contact_data.keys())
    for name in names:
        msg_header = f"Dear {name},\n"
        msg:str = asyncio.run(fetch_data())
        message = msg_header+msg+"\nFrom DanieL"
        at_sms.send([contact_data.get(name)],message)
        twilio_sms.send(config.sender,contact_data.get(name),message)

if __name__ == "__main__":
    main()