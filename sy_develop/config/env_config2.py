from enum import Enum

class Env_config(Enum):
    domain_mapping={
        'test':'http://10.16.32.77:39081',
        'pro':'http://develop.shenyanai.com:30080'

    }

    login_mapping = {
        'test': {
            "email":"fff@163.com",
            "password":"UUu6s6N5V65V5JnUbdT97fNQLtcyEvmPnu5Y9Oy1MII2NSao2N66oHeBKk2SLJO3JPaJDUGpiB0xiG9T0Z1pPQ"#deepblue2020
    },
        'pro': {
            "email":"fff@163.com",
            "password":"YBtadKKwgc+hrs4c6eAmOogKCl7LI2zCjh4o8o3c6W7SDqhaPazJ1dagDqoY+W8xwYvpuxYX4RmO2dDHIt5qGw=="
    }
    }


    redis_mapping={
        'test':{
            "REDIS_HOST":"10.16.32.77",
            "REDIS_PORT":"10000",
            "REDIS_PASSWD": "b94b4bfc",
            "DB": "1"
        },
        'pro': {
            "REDIS_HOST": "10.16.100.28",
            "REDIS_PORT": "30570",
            "REDIS_PASSWD": "deepblue2019",
            "DB": "0"
        }
    }

    mysql_mapping = {
        'test': {
            "MYSQL_HOST": "10.16.32.77",
            "MYSQL_PORT": 3306,
            "MYSQL_USER":"root",
            "MYSQL_PASSWD": "root",
            "MYSQL_DB": "dubhe-prod"
        },
        'pro': {
            "MYSQL_HOST": "10.16.100.28",
            "MYSQL_PORT": "30248",
            "MYSQL_USER": "dubhe-pro2",
            "MYSQL_PASSWD": "dubhe-pro2",
            "MYSQL_DB": "dubhe-pro"
        }
    }


if __name__ == '__main__':
    print(Env_config.mysql_mapping.value['test']['MYSQL_DB'])