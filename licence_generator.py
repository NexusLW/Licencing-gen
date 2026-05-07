import hmac
import hashlib
import base64

SECRET = "gobidiba-gooba-goobster"

def generate_license(email: str, expiry: str) -> str:
    data = f"{email}|{expiry}"

    hmac_bytes = hmac.new(
        SECRET.encode(),
        data.encode(),
        hashlib.sha256
    ).digest()

    hmac_b64 = base64.b64encode(hmac_bytes).decode()
    full = f"{data}|{hmac_b64}"

    return base64.b64encode(full.encode()).decode()

if __name__ == "__main__":
    email  = input("Email: ")
    expiry = input("Expiry (YYYY-MM-DD): ")
    key = generate_license(email, expiry)

    print("  LICENSE KEY")
    print("="*60)
    print(key)
    print("="*60 + "\n")