import requests
from config.env_config2 import *
from common.HttpRequest2 import HttpRequest2
from common.redis_operation import *
import json

#通过登录接口获取token
def get_code(get_env_value):
    domain=Env_config.domain_mapping.value[get_env_value]
    url=domain+'/development-platform/auth/code'
    httprequest = HttpRequest2(url)
    res1=httprequest.get()
    res=res1.json()
    uuid=res['data']['uuid']
    code=str(get(uuid,get_env_value),'utf-8')
    code.lstrip('"')
    code.rstrip('"')
    code=eval(code)
    logging.info('code is '+code)
    return uuid,code


#获取token
def get_token(get_env_value):
    headers = {
        "content-type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    domain = Env_config.domain_mapping.value[get_env_value]
    url=domain+'/development-platform/auth/login'
    logger.info("url是 "+url)
    uuid,code=get_code(get_env_value)
    email=Env_config.login_mapping.value[get_env_value]['email']
    password=Env_config.login_mapping.value[get_env_value]['password']
    data={
        "email":email,
          "password":password,
          "code":code,
          "uuid":uuid
    }
    #logger.info("登录入参data是 "+json.dumps(data))
    #logger.info("登录header是 "+str(headers))
    httprequest = HttpRequest2(url)
    res=httprequest.post(headers,json.dumps(data))
    res=res.json()
    logger.info('token是'+res['data']['token'])
    return res['data']['token']


if __name__ == '__main__':
    get_env='test'
    #print(get_code(get_env))
    print(get_token(get_env))



