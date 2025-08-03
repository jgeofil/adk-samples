import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("BASTEEN_API_KEY")
url = "https://api.basteen.ai/v1/truss"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}
response = requests.get(url, headers=headers)
print(response.json())
