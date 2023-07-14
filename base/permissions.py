from rest_framework.permissions import BasePermission

class GuestProfileApiPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.usertype in ['Frontdesk','Admin', 'Accounting']:
            return True
        else:
            return False
