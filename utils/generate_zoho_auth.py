import requests
import os

# get from https://api-console.zoho.eu/ or in GH secrets
CONFIG_ID = os.environ['ZOHO_CONFIG_ID']
CONFIG_SECRET = os.environ['ZOHO_CONFIG_SECRET']
CONFIG_CODE = os.environ['ZOHO_CONFIG_CODE']
REFRESH_TOKEN = os.environ['ZOHO_REFRESH_TOKEN']

if not CONFIG_CODE:
    exit("Visit https://api-console.zoho.eu/ and generate a CONFIG_CODE for a self client with scope `Desk.articles.CREATE, Desk.articles.UPDATE, Desk.articles.READ`")

BASE_URL = "https://accounts.zoho.eu/oauth/v2/token"
AUTH_URL = "{}?code={}&grant_type=authorization_code&client_id={}&client_secret={}&redirect_uri=https://www.qfield.cloud".format(BASE_URL, CONFIG_CODE, CONFIG_ID, CONFIG_SECRET)
REFRESH_URL = "{}?refresh_token={}&client_id={}&client_secret={}&scope=Desk.articles.CREATE,Desk.articles.UPDATE,Desk.articles.READ&grant_type=refresh_token".format(BASE_URL, REFRESH_TOKEN, CONFIG_ID, CONFIG_SECRET)
auth  = requests.post(REFRESH_URL)
try:
    print('access_token: ', auth.json()["access_token"])
    print('refresh_token: ', auth.json()["refresh_token"])
    
except KeyError:
    exit(auth.text)

