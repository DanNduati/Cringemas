import os
from os.path import join,dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__),'.env')
load_dotenv(dotenv_path,override=True)

#africas talking
username = os.environ.get('AT_USERNAME',None)
api_key = os.environ.get('AT_APIKEY',None)
short_code = os.environ.get('AT_SHORTCODE',None)

#twilio