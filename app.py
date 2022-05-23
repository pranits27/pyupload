import requests
import json

headers = {"Authorization": "Bearer ##Access Token##"} ## Put access token after the 'Bearer'
para = {
    "name": "##Name of file##", ## Name of the file
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