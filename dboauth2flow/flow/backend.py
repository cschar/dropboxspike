from django.contrib.auth.models import User


class CrappyDBXBackend(object):

    def authenticate(self, dbx_user_id=None):
        if not dbx_user_id or len(dbx_user_id.strip()) == 0:
            return None
        user, _ = User.objects.get_or_create(username=dbx_user_id)
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
