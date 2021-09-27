from common.excel_operation2 import *
from testcase2.conftest import *
from log.log import *
import json


ex=Exceloperation(excel_file1, sheet_name1)
@allure.story("查询用户得信息啊哈哈哈")
class TestInfo():

    @allure.title("哈哈哈，用户信息得标题呀1")
    @allure.description("1111111描述")
    def test_1(self,get_env_value):
        try:
            logger.info("当前使用环境为"+get_env_value)
            res1=fin_req_token(get_env_value, 1)
            res2=get_check_response(1)
            res1 = json.dumps(res1)#将dict转换为str
            logger.debug('网页得到'+res1)
            logger.debug('自己写的'+res2)
            assert res2[0:200] == res1[0:200]
        finally:
            ex.endsql_build_data(2, get_env_value)

    @pytest.mark.gai
    @allure.title("哈哈哈，用户信息得标题呀2")
    @allure.description("2222222描述")
    def test_2(self,get_env_value):
        try:
            ex.presql_build_data(2,get_env_value)
            res1 = fin_req_token(get_env_value, 2)
            res2 = get_check_response(2)
            res1 = json.dumps(res1,ensure_ascii=False)
            # 将dict转换为str
            logger.info(res2)
            logger.info(res2)
            assert res2[0:200] == res1[0:200]
        finally:
            ex.endsql_build_data(2,get_env_value)
            logger.info('运行完辣')


if __name__ == '__main__':
    a=TestInfo()
    print(a.test_1())