from config import ConfigClient


cc = ConfigClient(app_name='api', label='latest',
                  address='http://localhost:8888', profile='dev')
cc.get_config()

aaa = cc.get('aaa')
print(f"aaa: {aaa}")
