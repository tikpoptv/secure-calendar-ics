import secrets
import string

def generate_token(length=30):
    charset = string.ascii_letters + string.digits
    return ''.join(secrets.choice(charset) for _ in range(length))

print(generate_token())
