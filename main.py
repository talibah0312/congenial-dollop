from dotenv import load_dotenv
import os
import requests
import time

# Load variables from .env file
load_dotenv()

OWNER = 'talibah0312'
REPO = 'congenial-dollop'
WORKFLOW = 'main.yml'
REF = 'main'
PAT = os.getenv('PATSECRET')  # generate at github.com/settings/tokens

DISPATCH_URL = (
    f'https://api.github.com/repos/{OWNER}/{REPO}'
    f'/actions/workflows/{WORKFLOW}/dispatches'
)

headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {PAT}',
    'X-GitHub-Api-Version': '2022-11-28',
}

while True:
    time.sleep(21300)  # adjust cadence

    try:
        response = requests.post(
            DISPATCH_URL,
            headers=headers,
            json={'ref': REF},
        )
        # 204 No Content = success
        if response.status_code == 204:
            print("Dispatched OK (204)")
        else:
            print(f"Status: {response.status_code} — {response.text}")
    except Exception as e:
        print(f"Error: {e}")
