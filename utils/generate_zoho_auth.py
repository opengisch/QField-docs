import requests

# get from https://api-console.zoho.eu/
CONFIG_ID = ""
CONFIG_SECRET = ""
CONFIG_CODE = ""

if not CONFIG_CODE:
    exit("Visit https://api-console.zoho.eu/ and generate a CONFIG_CODE for a self client with scope `Desk.articles.CREATE, Desk.articles.UPDATE, Desk.tickets.ALL`")

AUTH_URL = "https://accounts.zoho.eu/oauth/v2/token?code={}&grant_type=authorization_code&client_id={}&client_secret={}&redirect_uri=https://www.qfield.cloud".format(CONFIG_CODE, CONFIG_ID, CONFIG_SECRET)
auth  = requests.post(AUTH_URL)
try:
    print('access_token: ', auth.json()["access_token"])
    print('refresh_token: ', auth.json()["refresh_token"])
    
except KeyError:
    exit(auth.text)

