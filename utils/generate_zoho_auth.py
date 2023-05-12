import os

import requests


CONFIG_ID = os.environ["ZOHO_CONFIG_ID"]
CONFIG_SECRET = os.environ["ZOHO_CONFIG_SECRET"]
CONFIG_CODE = os.environ["ZOHO_CONFIG_CODE"]
REFRESH_TOKEN = os.environ["ZOHO_REFRESH_TOKEN"]


BASE_URL = "https://accounts.zoho.eu/oauth/v2/token"


def create_access_secrets() -> dict[str, str] | None:
    """
    Used to generate CONFIG_CODE and REFRESH_TOKEN
    requires manual interaction.
    Before running it you need to create a valid auth on
    Visit https://api-console.zoho.eu/ and generate a new CONFIG_CODE
    for a self client with scope
    `Desk.articles.CREATE, Desk.articles.UPDATE, Desk.articles.READ`
    """

    url = "{}?code={}&grant_type=authorization_code&client_id={}&client_secret={}&redirect_uri=https://www.qfield.cloud".format(
        BASE_URL, CONFIG_CODE, CONFIG_ID, CONFIG_SECRET
    )
    auth = requests.post(url)
    try:
        access_token = auth.json()["access_token"]
        refresh_token = auth.json()["refresh_token"]
        tokens = {"access_token": access_token, "refresh_token": refresh_token}
        return tokens

    except KeyError:
        print(auth.text)
        print(
            "Visit https://api-console.zoho.eu/ and generate a new CONFIG_CODE for a self client with scope `Desk.articles.CREATE, Desk.articles.UPDATE, Desk.articles.READ`"
        )


def get_fresh_token() -> str | None:
    """used to get a new authentication code without manual interaction"""

    url = "{}?refresh_token={}&client_id={}&client_secret={}&scope=Desk.articles.CREATE,Desk.articles.UPDATE,Desk.articles.READ&grant_type=refresh_token".format(
        BASE_URL, REFRESH_TOKEN, CONFIG_ID, CONFIG_SECRET
    )
    auth = requests.post(url)

    try:
        token = auth.json()["access_token"]
        return token

    except KeyError:
        print(len(REFRESH_TOKEN))
        print(auth.text)


# print(get_fresh_token())
