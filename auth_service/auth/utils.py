import jwt
from datetime import datetime, timedelta
from ..common.config import Config


def generate_token(user: dict, expires_in: int = 24 * 60 * 60) -> str:
    """
    Generate a JWT token for the given user dictionary.
    The token contains the user's id, username, role, and permissions and
    expires after the specified interval (defaults to 24 hours).
    """
    payload = {
        'id': user.get('id'),
        'username': user.get('username'),
        'role': user.get('role'),
        'permissions': user.get('permissions', {}),
        'exp': datetime.utcnow() + timedelta(seconds=expires_in),
    }
    token = jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm='HS256')
    # PyJWT in version >=2 returns a string directly; older versions return bytes.
    return token if isinstance(token, str) else token.decode('utf-8')
