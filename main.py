from fastapi import FastAPI, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.routing import APIRoute
from dotenv import load_dotenv
from routers.salesforce import sf_router
import os

load_dotenv()

CONFIG = {
    "token_url": os.getenv('TOKEN_URL'),
    "client_id": os.getenv('CLIENT_ID'),
    "client_secret": os.getenv('CLIENT_SECRET'),
    "query_url": os.getenv('QUERY_URL')
}

app = FastAPI()
security = HTTPBasic()

app.include_router(sf_router)


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name  # in this case, operation ID will be 'greeting'


use_route_names_as_operation_ids(app)