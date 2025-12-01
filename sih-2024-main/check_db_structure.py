import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

headers = {"Authorization": f"Bearer {os.getenv('DIRECT_US_ACCESS_TOKEN')}"}

def check_structure():
    try:
        # Fetch one item from criminal_db
        response = requests.get("http://localhost:8055/items/criminal_db?limit=1", headers=headers)
        response.raise_for_status()
        data = response.json()
        if 'data' in data and len(data['data']) > 0:
            print("Criminal DB Item Keys:", data['data'][0].keys())
            print("Sample Item:", json.dumps(data['data'][0], indent=2))
        else:
            print("Criminal DB is empty or no data found.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_structure()
