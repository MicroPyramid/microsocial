Usage
=====

To get basic info from facebook
-------------------------------------------------------------

.. code-block:: python

    graph = facebook.GraphAPI(oauth_access_token)
    profile = graph.get_object("me")
    friends = graph.get_connections("me", "friends")
    graph.put_object("me", "feed", message="I am writing on my wall!")

If you are using the module within a web application with the JavaScript SDK, you can also use the module to use Facebook for login, parsing the cookie set by the JavaScript SDK for logged in users. For example, in Google AppEngine, you could get the profile of the logged in user with:

.. code-block:: python

    user = facebook.get_user_from_cookie(self.request.cookies, key, secret)
    if user:
        graph = facebook.GraphAPI(user["access_token"])
        profile = graph.get_object("me")
        friends = graph.get_connections("me", "friends")
        
        
To get pages in facebook
-----------------------------------------------------------------

.. code-block:: python

    from facebook import fb.py
    pages=get_fbpages(accesstoken)
    
    
To get groups in facebook
------------------------------------------------------------------

.. code-block:: python

    from facebook import fb.py
    groups=get_fbgroups(accesstoken)
    

To post on a page
-----------------------------------------------------------------

.. code-block:: python

    from facebook import fb.py
    postdata=post_on_page(pageid,pageaccesstoken,link,desc,msg,name,photourl,actionname,actionurl)


To post on a group
-----------------------------------------------------------------

.. code-block:: python

    from facebook import fb.py
    postdata=post_on_group(groupid,accesstoken,link,desc,msg,name,photourl,actionname,actionurl)
    

    
    
    
