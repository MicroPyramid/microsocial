#
class github(object):
    def __init__(self,app_id,app_secret,redirect_uri):
        self.access_token=''
        self.app_id=app_id
        self.app_secret=app_secret
        self.redirect_uri=redirect_uri
        self.host='https://github.com/login/oauth/'
        self.host1='https://api.github.com/'
        
    
    def authorize(self):
        rty  = self.host+"authorize?client_id=" + self.app_id
        rty +="&redirect_uri="+self.redirect_uri+"&scope=user,user:email,user:follow,repo,repo:status,delete_repo,notifications,gist&state=dia123456789ramya"
        return rty
    
    
    def get_accesstoken_from_code(self,code):
        params = {}
        params['grant_type'] = 'authorization_code'
        params['client_id'] = self.app_id
        params['redirect_uri'] = self.redirect_uri
        params['client_secret'] = self.app_secret
        params['code'] = code
        url=self.host+"access_token"
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
        data=self.send_request('get',self.host1+'user',params=params)
        return data
    
    
    def get_useremail(self):
        if self.access_token=='':
            error={'Error':'access token is not valid'}
            return error 
        params={'access_token':self.access_token}
        headers={'X-GitHub-Media-Type':'application/vnd.github.v3'}
        data=self.send_request('get',self.host1+"user/emails",params=params,headers=headers)
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
        if 'data' in response:
                response=response['data']
        
        return response
    
