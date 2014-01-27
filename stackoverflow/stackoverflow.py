import json
import urllib
import requests

class stackoverflow(object):
    def __init__(self,app_id,app_secret,app_key,redirect_uri,access_token=None):
        self.app_id=app_id
        self.app_secret=app_secret
        self.app_key=app_key
        self.redirect_uri=redirect_uri
        self.host='https://stackexchange.com/oauth'
        self.host1='https://api.stackexchange.com/2.1/me'
        if access_token:
            self.access_token=access_token
        else:
            self.access_token=''
        
    
    def authorize(self):
        rty  = self.host+"?client_id=" + self.app_id
        rty +="&redirect_uri="+self.redirect_uri+"&scope=no_expiry,write_access,read_inbox,private_info"
        return rty
    
    
    def get_accesstoken_from_code(self,code):
        params = {}
        params['grant_type'] = 'authorization_code'
        params['client_id'] = self.app_id
        params['redirect_uri'] = self.redirect_uri
        params['client_secret'] = self.app_secret
        params['code'] = code
        url=self.host+"/access_token"
        data=self.send_request('post',url,params=params)
        
        if 'access_token' in data:
            self.access_token=data['access_token']
            return data['access_token']
        return data
    
    
    def get_userinfo(self):
        if self.access_token=='':
            error={'Error':'access token is not valid'}
            return error 
        params={}
        params['access_token']=self.access_token
        params['site']="stackoverflow"
        params['key']=self.app_key 
        data=self.send_request('get',self.host1,params=params)
        return data
        
    
    def send_request(self,method,url,params=None,headers=None,timeout=60):
        if params is None:
            params=dict(format='json')
        else:
            params.update({'format':'json'})
         
        if headers is None:
            headers={}
             
        kw = dict(params=params,headers=headers, timeout=timeout)
         
        response=requests.request(method.upper(),url, **kw)
        response=response.json()
        return response
