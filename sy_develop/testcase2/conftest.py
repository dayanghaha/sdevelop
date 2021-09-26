from common.excel_operation2 import Exceloperation
from common.get_token import *
from log.log import *
from config.address_config import *
import pytest
import allure


#添加命令行参数--env，固定写法
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default='test',
        help="set env"
    )


#获取命令行参数的值,固定写法
@pytest.fixture(scope='session')
def get_env_value(request):
    return request.config.getoption('--env')
    print("当前的执行环境：%s" % request.config.getoption('--env'))



"""@pytest.fixture(scope='session')
def get_env_value(request):
    env = request.getfixturevalue("get_env")
    return env"""



#根据命令行选择的环境名称，根据token请求接口
def fin_req_token(get_env_value,case_number):
    token=get_token(get_env_value)
    url_domain=Env_config.domain_mapping.value[get_env_value]
    ex_op = Exceloperation(excel_file1, sheet_name1)
    res = ex_op.fact_result_token(case_number, token, url_domain)
    #logger.info(res)
    #logger.info(type(res))
    #这里是不是可以加try、except，保存错误信息
    #logger.info(res.json())
    return res.json()



##获取excel中预期结果
#@pytest.fixture(scope='function')
def get_check_response(case_number):
    ex_op1 = Exceloperation(excel_file1, sheet_name1)
    res=ex_op1.check_result(case_number)
    return res

