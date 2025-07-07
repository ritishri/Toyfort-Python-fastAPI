from jose import jwt
from datetime import datetime,timedelta


SECERET_KEY = "secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 2


def create_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp":expire})
    encode_jwt = jwt.encode(to_encode, SECERET_KEY,algorithm=ALGORITHM)
    return encode_jwt