Python LinkedIn
=================

Python interface to the LinkedIn API

This library provides a pure Python interface to the LinkedIn **Profile**, **Group**, **Company**, **Jobs**, **Search**, **Share**, **Network** and **Invitation** REST APIs.

`LinkedIn <http://developer.linkedin.com>`_ provides a service that lets people bring their LinkedIn profiles and networks with them to your site or application via their OAuth based API. This library provides a lightweight interface over a complicated LinkedIn OAuth based API to make it for python programmers easy to use.



Authentication
-----------------------

LinkedIn REST API uses **Oauth 2.0** protocol for authentication. In order to use the LinkedIn API, you have an **application key** and **application secret**. You can get more detail from `here <http://developers.linkedin.com/documents/authentication>`_.

For debugging purposes you can use the credentials below. It belongs to my test application. Nothing's harmful.

.. code-block:: python

    KEY = 'your app key'
    SECRET = 'your app secret'


LinkedIn redirects the user back to your website's URL after granting access (giving proper permissions) to your application. We call that url **RETURN URL**. Assuming your return url is **http://localhost:8000**, you can write something like this:

.. code-block:: python

    from linkedin import linkedin

    API_KEY = "your app key"
    API_SECRET = "your app secret"
    RETURN_URL = "redirect url"
    authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
    print authentication.authorization_url
    application = linkedin.LinkedInApplication(authentication)

When you grant access to the application, you will be redirected to the return url with the following query strings appended to your **RETURN_URL**:

.. code-block:: python

    "RETURN_URL/?code=AQTXrv3Pe1iWS0EQvLg0NJA8ju_XuiadXACqHennhWih7iRyDSzAm5jaf3R7I8&state=ea34a04b91c72863c82878d2b8f1836c"


This means that the value of the **authorization_code** is **AQTXrv3Pe1iWS0EQvLg0NJA8ju_XuiadXACqHennhWih7iRyDSzAm5jaf3R7I8**. After setting it by hand, we can call the **.get_access_token()** to get the actual token.

.. code-block:: python

    authentication.authorization_code = "AQTXrv3Pe1iWS0EQvLg0NJA8ju_XuiadXACqHennhWih7iRyDSzAm5jaf3R7I8"
    authentication.get_access_token()


Quick Usage From Python Interpreter
---------------------------------------------------------

For testing the library using an interpreter, use the quick helper.

.. code-block:: python

    from linkedin import server
    application = server.quick_api(KEY, SECRET)

This will print the authorization url to the screen. Go into this URL using a browser, after you login, the method will return with an API object you can now use.

.. code-block:: python

    application.get_profile()
    
Profile API
---------------------------------------------------------------

The Profile API returns a member's LinkedIn profile. You can use this call to return one of two versions of a user's profile which are **public profile** and **standart profile**. For more information, check out the [documentation](http://developers.linkedin.com/documents/profile-api).

.. code-block:: python

    application.get_profile()


There are many **field selectors** that enable the client fetch more information from the API. All of them used by each API are listed [here](http://developers.linkedin.com/documents/field-selectors).

.. code-block:: python
    application.get_profile(selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations'])


Connections API
----------------------------------------------------------------

The Connections API returns a list of **1st degree** connections for a user who has granted access to their account. For more information, you check out its [documentation](http://developers.linkedin.com/documents/connections-api).

To fetch your connections, you simply call **.get_connections()** method with proper GET querystring:

.. code-block:: python
    application.get_connections()
    application.get_connections(selectors=['headline', 'first-name', 'last-name'], params={'start':10, 'count':5})


Search API
----------------------------------------------------------------

here are 3 types of Search APIs. One is the **People Search** API, second one is the **Company Search** API and the last one is **Jobs Search** API.

The People Search API returns information about people. It lets you implement most of what shows up when you do a search for "People" in the top right box on LinkedIn.com.
You can get more information from [here](http://developers.linkedin.com/documents/people-search-api).

.. code-block:: python
     application.search_profile(selectors=[{'people': ['first-name', 'last-name']}], params={'keywords': 'apple microsoft'})
     # Search URL is https://api.linkedin.com/v1/people-search:(people:(first-name,last-name))?keywords=apple%20microsoft


The Company Search API enables search across company pages. You can get more information from [here](http://developers.linkedin.com/documents/company-search).

.. code-block:: python
     application.search_company(selectors=[{'companies': ['name', 'universal-name', 'website-url']}], params={'keywords': 'apple microsoft'})
     # Search URL is https://api.linkedin.com/v1/company-search:(companies:(name,universal-name,website-url))?keywords=apple%20microsoft


The Job Search API enables search across LinkedIn's job postings. You can get more information from [here](http://developers.linkedin.com/documents/job-search-api).

.. code-block:: python
    application.search_job(selectors=[{'jobs': ['id', 'customer-job-code', 'posting-date']}], params={'title': 'python', 'count': 2})


Group API
---------------------------------------------------------------------

The Groups API provides rich access to read and interact with LinkedIn’s groups functionality. You can get more information from [here](http://developers.linkedin.com/documents/groups-api). By the help of the interface, you can fetch group details, get your group memberships as well as your posts for a specific group which you are a member of.

.. code-block:: python
    application.get_group(41001)
    application.get_memberships(params={'count': 20})
    application.get_posts(41001)

You can also submit a new post into a specific group.

.. code-block:: python
    title = 'your title'
    summary = 'your summary'
    submitted_url = 'url to submit'
    submitted_image_url = 'image url'
    description = 'description about the post'
    application.submit_group_post(41001, title, summary, submitted_url, submitted_image_url, description)
    

Company API
-----------------------------------------------------------------------

The Company API:
 * Retrieves and displays one or more company profiles based on the company ID or universal name.
 * Returns basic company profile data, such as name, website, and industry.
 * Returns handles to additional company content, such as RSS stream and Twitter feed.

You can query a company with either its **ID** or **Universal Name**. For more information, you can check out the documentation [here](http://developers.linkedin.com/documents/company-lookup-api-and-fields).

.. code-block:: python
    application.get_companies(company_ids=[1035], universal_names=['apple'], selectors=['name'], params={'is-company-admin': 'true'})
    
    # Get the latest updates about Microsoft
    application.get_company_updates(1035, params={'count': 2})


You can follow or unfollow a specific company as well.

.. code-block:: python
    application.follow_company(1035)
    True

    application.unfollow_company(1035)
    True


Job API
-------------------------------------------------------------------------

The Jobs APIs provide access to view jobs and job data. You can get more information from its [documentation](http://developers.linkedin.com/documents/job-lookup-api-and-fields).

.. code-block:: python
    application.get_job(job_id=5174636)
    
You can also fetch you job bookmarks.

.. code-block:: python
application.get_job_bookmarks()


Share API
--------------------------------------------------------------------------

Network updates serve as one of the core experiences on LinkedIn, giving users the ability to share rich content to their professional network. You can get more information from [here](http://developers.linkedin.com/documents/share-api).

.. code-block:: python
application.submit_share('Posting from the API using JSON', 'A title for your share', None, 'http://www.linkedin.com', 'http://d.pr/3OWS')
{'updateKey': u'UNIU-8219502-5705061301949063168-SHARE'
 'updateURL': 'http://www.linkedin.com/updates?discuss=&amp;scope=8219502&amp;stype=M&amp;topic=5705061301949063168&amp;type=U&amp;a=aovi'}


Network API
---------------------------------------------------------------------------

The Get Network Updates API returns the users network updates, which is the LinkedIn term for the user's feed. This call returns most of what shows up in the middle column of the LinkedIn.com home page, either for the member or the member's connections. You can get more information from [here](http://developers.linkedin.com/documents/get-network-updates-and-statistics-api).

There are many network update types. You can look at them by importing **NETWORK_UPDATES** enumeration.

.. code-block:: python
    from linkedin.linkedin import NETWORK_UPDATES
    print NETWORK_UPDATES.enums
    update_types = (NETWORK_UPDATES.CONNECTION, NETWORK_UPDATES.PICTURE)
    application.get_network_updates(update_types)


Invitation API
-----------------------------------------------------------------------------

The Invitation API allows your users to invite people they find in your application to their LinkedIn network. You can get more information from [here](http://developers.linkedin.com/documents/invitation-api).

.. code-block:: python
    from linkedin.models import LinkedInRecipient, LinkedInInvitation
    recipient = LinkedInRecipient(None, 'john.doe@python.org', 'John', 'Doe')
    print recipient.json
    invitation = LinkedInInvitation('Hello John', "What's up? Can I add you as a friend?", (recipient,), 'friend')
    print invitation.json
    application.send_invitation(invitation)


More
-----------------
For more information, visit the `homepage <http://ozgur.github.com/python-linkedin/>`_ of the project.
