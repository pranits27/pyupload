import requests
import json
from datetime import datetime

headers = {"Authorization": "Bearer ##Access Token##"} ## Put access token after the 'Bearer'
now = datetime.now()
para = {
    "name": "##Name of file##" +str(now), ## Name of the file
    "parents": ["##folder id##"] ## Add folder id
}

files = {
    'data': ('metadata', json.dumps(para), ' application/json; charset=UTF-8'),
    'file': ('application/zip',open("./zip", "rb"))  ## Replace path and file on ./zip
}

r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)

print(r.text)
