# fastapi-miocroservice-infrastructure

## services list

### middleware
- mysqldb
- rabbitmq
- redis
- flower
### services
- config-server:
    spring cloud config，配置中心
- app1-service:
    fastapi 用來實作config-server 和 easyauth-server的client。
- auth-server
    fastapi 用來實作easyauth-server。
- easyauth
    用打包好的easyauth docker image來架設easyauth-server。

### others
- clientapp.py
    用來測試app1-service的client。

## how to run
可以用下面指令來建置和啟動所有服務，又或者可以用`ctrl`+`shift`+`B`來執行預設建置任務。

```bash
docker-compose up -d
```