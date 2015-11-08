from django.conf import settings
from django.contrib.auth.models import check_password
from accounts.models import MyUser


class EmailAuthBackend(object):
    """
    A custom authentication backend. Allows users to log in using their email address.
    """

    def authenticate(self, email=None, password=None):
        """
        Authentication method
        """
        try:
            user = MyUser.objects.get(email=email)
            # if user.check_password(password):
            # 	print "OK"
            #     return user
            if user.password == password:
                print "OK"
                return user

        except MyUser.DoesNotExist:
        	print "Password is wrong. Return none."
        	return None

    def get_user(self, user_id):
        try:
            user = MyUser.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except MyUser.DoesNotExist:
            return None