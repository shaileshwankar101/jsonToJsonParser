import jwt
import datetime
import secrets

secret_key = secrets.token_hex(32)
user_data = {
    "user_id": 123,
    "user_name": "MollyHolly"
}

expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

token = jwt.encode(
    {"user": user_data, "exp": expiration_time},
    secret_key,
    algorithm="HS256"
)

print("Generated Token", token)

try:
    decode_token = jwt.decode(token, secret_key, algorithms="HS256")
    print("Token Decoded", decode_token)

except jwt.ExpiredSignatureError:
    print("Token Expired")

except jwt.InvalidTokenError:
    print("Invalid Token")
