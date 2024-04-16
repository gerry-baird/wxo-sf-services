import os
import requests
import json
from fastapi import APIRouter
from dotenv import load_dotenv
from models.Account import Account, AccountList

sf_router = APIRouter()
load_dotenv()
CONFIG = {
    "token_url": os.getenv('TOKEN_URL'),
    "client_id": os.getenv('CLIENT_ID'),
    "client_secret": os.getenv('CLIENT_SECRET'),
    "query_url": os.getenv('QUERY_URL')
}

AUTH_DATA = {
    'grant_type': 'client_credentials',
    'client_id': CONFIG["client_id"],
    'client_secret': CONFIG["client_secret"]
}

def get_token():
    # Get the access token here
    try:
        response = requests.post(CONFIG["token_url"], data=AUTH_DATA)
        access_token = response.json()['access_token']
        if not access_token:
            raise ValueError('Bearer token could not be retrieved.')
    except ValueError as e:
        print(e)

    return access_token

def fetch_data(token: str, query: str):
    response = ""

    auth_value = f"Bearer {token}"
    headers = {
        'Content-type': 'application/json',
        'Accept-Encoding': 'gzip',
        'Authorization': auth_value
    }

    response = requests.get(CONFIG["query_url"], headers=headers, params={"q":query})

    return response.json()


@sf_router.get("/top_accounts",
               summary='Accounts with largest revenue',
               description='Get a list of accounts with the largest revenue')
def top_accounts() -> AccountList:
    token = get_token()
    query = "SELECT Name, AnnualRevenue FROM Account WHERE AnnualRevenue > 0 ORDER BY AnnualRevenue DESC"

    raw_response = fetch_data(token, query)

    # get record list
    records = raw_response["records"]

    temp_list = []
    record_count = len(records)
    for count, value in enumerate(records):
        account_name = value["Name"]
        revenue = value["AnnualRevenue"]
        acc = Account(name=account_name, revenue=revenue)
        temp_list.append(acc)

    account_list = AccountList(accounts=temp_list, totalSize=record_count)

    return account_list
