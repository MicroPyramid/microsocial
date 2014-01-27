from linkedin.linkedin import (LinkedInAuthentication, LinkedInApplication,
                               PERMISSIONS)



API_KEY = 'your app key'
API_SECRET = 'your app secret'
RETURN_URL = 'your redirect uri'
authentication = LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL,
                                    PERMISSIONS.enums.values())
print authentication.authorization_url
application = LinkedInApplication(authentication)
