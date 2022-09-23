import os
from dotenv import load_dotenv

load_dotenv()

GCP_PROJECT_ID = os.getenv('GCP_PROJECT_ID')
SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')
STORAGE_BUCKET_NAME = os.getenv('STORAGE_BUCKET_NAME')

# from dotenv import load_dotenv
# from pathlib import Path

# dotenv_path = Path('.env')
# load_dotenv(dotenv_path=dotenv_path)

print(GCP_PROJECT_ID)