from account.models import Account
from django.contrib.auth.backends import ModelBackend
import logging


class MyAuthBackend(ModelBackend):

    def authenticate(self, mobile_number=None, password=None, **kwargs):

        try:
            user = Account.objects.get(mobile_number=mobile_number)
            if user.check_password(password):
                return user
            else:
                return None
        except ObjectDoesNotExist:
            pass
        # except Account.DoesNotExist:
        #     logging.getLogger("error_logger").error("user with login %s does not exists " % login)
        #     return None
        # except Exception as e:
        #     logging.getLogger("error_logger").error(repr(e))
        #     return None

    # def get_user(self, user_id):
    #     try:
    #         user = Account.objects.get(sys_id=user_id)
    #         if user.is_active:
    #             return user
    #         return None
    #     except Account.DoesNotExist:
    #         logging.getLogger("error_logger").error("user with %(user_id)d not found")
    #         return None
