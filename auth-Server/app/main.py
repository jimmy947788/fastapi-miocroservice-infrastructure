import logging
from fastapi import Depends, FastAPI, Request

from easyauth.server import EasyAuthServer
from config import ConfigClient
from config.ext.fastapi import fastapi_config_client
from config.logger import logger

logging.basicConfig(level=logging.DEBUG)
server = FastAPI(dependencies=[Depends(fastapi_config_client)])


server.auth = EasyAuthServer.create(
    server,
    '/auth/token',
    auth_secret='abcd1234',
    admin_title='EasyAuth - Company',
    admin_prefix='/admin',
    env_from_file='server_env.json'
)
