#
import json
import urllib
import requests
import gdata.contacts.client

class google(object):
    def __init__(self,app_id,app_secret,redirect_uri,access_token=None):
        self.app_id=app_id
        self.app_secret=app_secret
        self.redirect_uri=redirect_uri
        self.host='https://accounts.google.com/o/oauth2/'
        self.host1='https://www.googleapis.com/oauth2/v1/'
        if access_token:
            self.access_token=access_token
        else:
            self.access_token=''
        
    
    def authorize(self):
        rty  = self.host+"auth?client_id=" + self.app_id + "&response_type=code"
        rty +="&redirect_uri="+self.redirect_uri+"https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email https://www.google.com/m8/feeds/contacts/&state=dia123456789ramya"
        return rty
    
    
    def get_accesstoken_from_code(self,code):
        params = {}
        params['grant_type'] = 'authorization_code'
        params['client_id'] = self.app_id
        params['redirect_uri'] = self.redirect_uri
        params['client_secret'] = self.app_secret
        params['code'] = code
        url=self.host + "token"
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
        data=self.send_request('get',self.host1+'userinfo',params=params)
        return data
        
    def get_usercontacts(self):
        auth_token=gdata.gauth.OAuth2Token(client_id=self.app_id,
                                 client_secret=self.app_secret,
                                 scope='https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email https://www.google.com/m8/feeds/contacts/ ',
                                 user_agent='dummy-sample'
                                  
                               )
        auth_token.access_token=self.access_token
        client1=gdata.contacts.client.ContactsClient(source='')
        client1=auth_token.authorize(client1)
        qry = gdata.contacts.client.ContactsQuery(max_results=3000)
        feed = client1.get_contacts(query=qry)
        data=[]
        f1={}
        emaillist=[]
        for entry in feed.entry:
          f1={}
          f1['id']=entry.id.text
          if not entry.name is None:
              if not entry.name.full_name is None:
                  f1['fullname']=entry.name.full_name.text
              if not entry.name.family_name is None:
                  f1['familyname']= entry.name.family_name.text
        
          if not entry.title is None:
              if entry.title.text!=None:
                  f1['title']=entry.title.text
                
          for email in entry.email:
              emaillist.append(email)
              f1['email']=email.address
          for phone in entry.phone_number:
              f1['phone']=phone.text
          data.append(f1.copy())
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
