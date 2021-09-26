from testcase2.conftest import *
from common.HttpRequest2 import HttpRequest2
from xlutils import copy
import xlrd

from common.mysql_operation import query_db
from log.log import *
import json



class Exceloperation():
    def __init__(self,excel_file,sheet_name):
        self.excel_file=excel_file
        self.sheet_name=sheet_name

#将excel数据转换为列表,并通过number获取某一条用例
    def get_excel_case(self,case_number):
        wb=xlrd.open_workbook(self.excel_file)
        sh=wb.sheet_by_name(self.sheet_name)
        exlist=[]
        for i in range(1,sh.nrows):
            datarows=dict(zip(sh.row_values(0),sh.row_values(i)))#将数据和标题组装成字典
            exlist.append(datarows)
        #通过number获取某一条用例
        for case_data in exlist:
            if case_number == case_data['number']:
                return case_data


#将值存入excel
    def save_to_excel(self,case_number,data):
        rbook = xlrd.open_workbook(self.excel_file)
        wbook = copy.copy(rbook)
        sheet_number=wbook.sheet_index(self.sheet_name)
        w_sheet=wbook.get_sheet(sheet_number)
        w_sheet.write(case_number+1,10,data)
        wbook.save(self.excel_file)



#若是需要数据库中添加数据，则执行，若为空则不执行
    def presql_build_data(self,case_number,get_env_value):
        case_data = self.get_excel_case(case_number)
        presql=case_data['presql']
        if presql == '':
            pass
        else:
            query_db(presql,get_env_value)


#若是需要数据库中删除数据，则执行，若为空则不执行
    def endsql_build_data(self,case_number,get_env_value):
        case_data = self.get_excel_case(case_number)
        endsql=case_data['endsql']
        if endsql == '':
            pass
        else:
            query_db(endsql,get_env_value)


#获取excel中预期结果
    def check_result(self,case_number):
        case_data = self.get_excel_case(case_number)
        response = case_data['response']
        return response


#带有token的请求
    def fact_result_token(self,case_number,token,url_domain):
        case_data=self.get_excel_case(case_number)
        if case_data is None:
            logging.info('case can not found')
        params = case_data['parament']
        url = url_domain+case_data['url']
        headers=case_data['header']
        headers=json.loads(headers)

        httprequest=HttpRequest2(url)
        if case_data['method'] == 'get':
            res=httprequest.get(headers=headers,token=token)
        elif case_data['method'] == 'post':
            res=httprequest.post(headers,params,token=token)
        elif case_data['method'] == 'put':
            res = httprequest.put(headers, params, token=token)
        else:
            logger.info('the method is not get or post or put,please check fb')
        return res



if __name__ == '__main__':
    """a=Exceloperation(excel_file1,sheet_name1)
    b=a.get_excel_case(1)
    if b['presql']=='':
        print('aaaa')"""