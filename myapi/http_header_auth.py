from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

from myapi.core.models import Role, Privilege

class HttpHeaderAuthentication(authentication.BaseAuthentication):
    
    def do_auth(self, user_roles):
        # check database
        prives = Privilege.objects.raw('select p.* from privileges p inner join roles r on p.role_id = r.role_id where r.role_name = %s',[user_roles])
        privileges = []
        for p in prives:
            privileges.append(p.priv_name)
        if (len(privileges)==0): 
            # no roles available, this user shouldnt have come this far
            # user has no roles so we won't give any response
            print("No roles found")
            return [] 
        return privileges

    
    def authenticate(self, request):
        print("Auth service invoked")
        user_roles = request.headers.get('HTTP-USER-GROUPS-FIELD')
        privileges_from_db = self.do_auth(user_roles)
        print(f"found {len(privileges_from_db)} privileges for user_roles {user_roles}")

        u = User()
        u.Meta.groups = privileges_from_db # to set in response headers using myapi.request_control_middleware.AuthMiddleware class

        if(len(privileges_from_db)==0):
            print("no privileges found")
            raise exceptions.AuthenticationFailed('no privileges available')


        return (u, None) # authentication successful
    

