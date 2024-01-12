import requests
import os
from dotenv import load_dotenv

def upload_to_pinata():
    load_dotenv()
    file_path = '../certificate-generation/images/generated_certificate.jpg'
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    jwt_token = os.getenv("PINATA_API_KEY")
    headers = {"Authorization": f"Bearer {jwt_token}"}

    with open(file_path, "rb") as fp:
        response = requests.post(url, files={"file": fp}, headers=headers)
        return response.json()