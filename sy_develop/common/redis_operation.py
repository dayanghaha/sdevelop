import redis
from config.env_config2 import *
from log.log import *

def get(key,get_env_value):
    re = redis.Redis(host=Env_config.redis_mapping.value[get_env_value]['REDIS_HOST'],
                     port=Env_config.redis_mapping.value[get_env_value]['REDIS_PORT'],
                     password=Env_config.redis_mapping.value[get_env_value]['REDIS_PASSWD'],
                     db=Env_config.redis_mapping.value[get_env_value]['DB'])

    return re.get(key)




if __name__ == '__main__':
    e='test'
    key='validate_codecd19d6af09954f97bdb3384366a53376'
    print(get(key,e))

