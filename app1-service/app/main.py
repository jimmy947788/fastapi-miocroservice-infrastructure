import logging
from easyauth import get_user
from easyauth.client import EasyAuthClient

from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse

# from config import ConfigClient
from config.ext.fastapi import fastapi_config_client
from config.logger import logger


logging.basicConfig(level=logging.DEBUG)
server = FastAPI(dependencies=[Depends(fastapi_config_client)], debug=True)

server.auth = EasyAuthClient.create(
    server,
    token_server="easyauth.local",
    token_server_port=8220,
    auth_secret="abcd1234",
    default_permissions={"groups": ["users"]},
)


# @server.auth.get("/", response_class=HTMLResponse)
# def home():
#     return """
#     <html>
#       <body>
#       <p>config-client | FastAPI integration</p>
#       <p>sample endpoints</p>
#       <ul>
#         <li>/config/<my.property></li>
#         <ul>
#           <li><a href="http://localhost:8000/config/spring">/config/spring</a></li>
#           <li><a href="http://localhost:8000/config/health">/health</a></li>
#           <li><a href="http://localhost:8000/config/spring.cloud.consul">/spring/cloud/consul</a></li>
#         </ul>
#         <li><a href="http://localhost:8000/info">/info</a></li>
#       </ul>
#       </body>
#     </html>
#     """


# @app.get("/info")
# def consul(request: Request):
#     return dict(
#         description=request.app.config_client.get("info.app.description"),
#         url=request.app.config_client.get("info.app.name"),
#     )


# @app.get("/config/{config_key}")
# def config(request: Request, config_key):
#     return request.app.config_client.get(f"{config_key}", {"message": "not found"})


# grants access to only specified users
@server.auth.get("/", users=["jane"])
async def root():
    return f"I am root"


# grants access to members of 'users' or 'admins' group.
@server.auth.get("/groups", groups=["users", "admins"])
async def groups(user: str = get_user()):  # type: ignore
    return f"{user} is in groups"


# grants access to all members of 'users' group
# or a groups with role of 'basic' or advanced
@server.auth.get("/roles", roles=["basic", "advanced"], groups=["users"])
async def roles():
    return f"Roles and Groups"


# grants access to all members of groups with a roles granting 'BASIC_CREATE'
@server.auth.get("/actions", actions=["BASIC_CREATE"])
async def action():
    return f"I am actions"
