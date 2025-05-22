import binascii
import os
from .models import ExpiringToken

# Contains a utility function to generate or refresh user tokens.

def generate_token(user):
    token_key = binascii.hexlify(os.urandom(20)).decode()
    token, _ = ExpiringToken.objects.update_or_create(
        user=user,
        defaults={'key': token_key}
    )
    return token
