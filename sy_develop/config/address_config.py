import time
import os

#该工程的路径
proj_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#日志路径，更改路径到log目录下,按天生成log
today=time.strftime('%Y%m%d',time.localtime())
log_file=os.path.join(proj_path,'log','log_{}.txt'.format(today))

#测试用例excel路径
excel_file1=os.path.join(proj_path,'data','MetaMind_api_test.xlsx')
sheet_name1='meta'

#report=os.path.join(proj_path,'report')
