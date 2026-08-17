import secrets
import string


def generate_id(prefix: str) -> str:
    characters = string.ascii_letters + string.digits

    random_part = "".join(
        secrets.choice(characters)
        for _ in range(8)
    )

    return f"{prefix}_{random_part}"