import requests
import json

def get_fbpages(accesstoken):
  u=requests.get("https://graph.facebook.com/me/accounts",params={'access_token':accesstoken})
  pagese= u.json()
  if 'data' in pages:
    return pages['data']
  else:
    return pages
    
def get_fbgroups(accesstoken):
    u=requests.get("https://graph.facebook.com/me/groups",params={'access_token':accesstoken})
    groups= u.json()
    if 'data' in groups:
      return groups['data']
    else:
      return groups
      
def post_on_page(pageid,page_accesstoken,desc,link=None,name=None,msg=None,purl=None,action_name=None,action_url=None):
    params = {}
    params['access_token']=page_accesstoken
    params['description']=desc
    if link:
      params['link']= link
    if msg:
      params['message'] = msg 
    if name:
      params['name']= name
    if purl:
      params['picture']= purl
    if action_name:
      if action_url:
        params['actions']=[{'name': action_name, 'link':action_url}]
      else:
        if link:
          params['actions']=[{'name': action_name, 'link':link}]
    params = urllib.urlencode(params)
    response = urllib.urlopen("https://graph.facebook.com/" + pageid + "/feed", params).read()
    response=json.loads(response)
    return response
    

def post_on_group(groupid,accesstoken,desc,link=None,name=None,msg=None,purl=None,action_name=None,action_url=None):
    params = {}
    params['access_token']=accesstoken
    params['description']=desc
    if link:
      params['link']= link
    if msg:
      params['message'] = msg 
    if name:
      params['name']= name
    if purl:
      params['picture']= purl
    if action_name:
      if action_url:
        params['actions']=[{'name': action_name, 'link':action_url}]
      else:
        if link:
          params['actions']=[{'name': action_name, 'link':link}]
    params = urllib.urlencode(params)
    response = urllib.urlopen("https://graph.facebook.com/" + groupid + "/feed", params).read()
    response=json.loads(response)
    return response
