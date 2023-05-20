import logging

from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse

from config import ConfigClient
from config.ext.fastapi import fastapi_config_client
from config.logger import logger

logging.basicConfig(level=logging.DEBUG)
app = FastAPI(dependencies=[Depends(fastapi_config_client)])


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
      <body>
      <p>config-client | FastAPI integration</p>
      <p>sample endpoints</p>
      <ul>
        <li>/config/<my.property></li>
        <ul>
          <li><a href="http://localhost:8000/config/spring">/config/spring</a></li>
          <li><a href="http://localhost:8000/config/health">/health</a></li>
          <li><a href="http://localhost:8000/config/spring.cloud.consul">/spring/cloud/consul</a></li>
        </ul>
        <li><a href="http://localhost:8000/info">/info</a></li>
      </ul>
      </body>
    </html>
    """


@app.get("/info")
def consul(request: Request):
    return dict(
        description=request.app.config_client.get("info.app.description"),
        url=request.app.config_client.get("info.app.name"),
    )


@app.get("/config/{config_key}")
def config(request: Request, config_key):
    return request.app.config_client.get(f"{config_key}", {"message": "not found"})
