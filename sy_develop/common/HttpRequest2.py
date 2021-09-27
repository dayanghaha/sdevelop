import requests
from log.log import *

class HttpRequest2():
    def __init__(self,url):
        self.url=url
        self.requests=requests.session()

    def get(self,headers=None,token=None):
        if token is not None :
            headers['Authorization']=token
            return self.requests.get(url=self.url,headers=headers)
        #logger.info(headers)
        return self.requests.get(url=self.url)

    def post(self,headers,datas,token=None):
        if token is not None:
            headers['Authorization']=token
        return self.requests.post(url=self.url,headers=headers,data=datas)

    def delete(self,headers,token=None):
        if token is not None:
            headers['Authorization']=token
        return self.requests.delete(url=self.url)

    def put(self,headers,datas,token=None):
        if token is not None:
            headers['Authorization']=token
        return self.requests.put(url=self.url,data=datas,headers=headers)


if __name__=='__main__':    #请求官网
    import json
    a=HttpRequest2("https://www.shenyanai.com/website-management/cooperation/consultation/save")
    data = {"company": "1", "contactPhone": "15651111111", "description": "1"}
    b=a.post({"Content-Type":"application/json;charset=UTF-8"},json.dumps(data))
    print(b.text)
    print(b.status_code)