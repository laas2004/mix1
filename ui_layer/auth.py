import hashlib

# change this later
_ADMIN_PASSWORD = "admin123"

def check_admin_password(password: str) -> bool:
    hashed = hashlib.sha256(password.encode()).hexdigest()
    expected = hashlib.sha256(_ADMIN_PASSWORD.encode()).hexdigest()
    return hashed == expected
