import pymysql
from config.env_config2 import *
from testcase2.conftest import *
from log.log import *

def query_db(sql,get_env_value):
    db = pymysql.connect(host=Env_config.mysql_mapping.value[get_env_value]['MYSQL_HOST'],
                         port=Env_config.mysql_mapping.value[get_env_value]['MYSQL_PORT'],
                         user=Env_config.mysql_mapping.value[get_env_value]['MYSQL_USER'],
                         passwd=Env_config.mysql_mapping.value[get_env_value]['MYSQL_PASSWD'],
                         db=Env_config.mysql_mapping.value[get_env_value]['MYSQL_DB'],
                         charset='utf8')
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db_get_results = cursor.fetchall()  # 获取所有记录列表
    logging.debug(db_get_results)
    cursor.close()
    db.close()

"""def change_db(sql,get_env):
    db = pymysql.connect(host=Env_config.mysql_mapping.value[get_env]['MYSQL_HOST'],
                         port=Env_config.mysql_mapping.value[get_env]['MYSQL_PORT'],
                         user=Env_config.mysql_mapping.value[get_env]['MYSQL_USER'],
                         passwd=Env_config.mysql_mapping.value[get_env]['MYSQL_PASSWD'],
                         db=Env_config.mysql_mapping.value[get_env]['MYSQL_DB'],
                         charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as eee:
        logging.error(eee)
    finally:
        cursor.close()
        db.close()"""


if __name__ == '__main__':
    q="select * from data_dataset where id=101"
    w='delete from users_roles where user_id=155;'
    e='test'
    query_db(w,e)