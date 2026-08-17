from app.auth.security import (
    create_access_token,
    decode_access_token,
    hash_password,
    verify_password,
)

password = "ResumeAI123"

hashed = hash_password(password)

print("Hashed Password:")
print(hashed)

print()

print("Password Match:")
print(verify_password(password, hashed))

print()

token = create_access_token(
    {
        "sub": "john@example.com"
    }
)

print("JWT Token:")
print(token)

print()

payload = decode_access_token(token)

print("Decoded Payload:")
print(payload)