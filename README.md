# pyupload
Uploading file on gdrive using Python

## First of all you need to enable Google drive API:

1. Log into google developer console at https://console.cloud.google.com/apis/dashboard.
2. Click select project at the right side of “Google Cloud Platform” of upper left of window.
3. If you cannot see the project, please try to access to https://console.cloud.google.com/cloud-resource-manager.

#### You can also create new project at there. When you create a new project there, please click the left of “Google Cloud Platform”. You can see it like 3 horizontal lines.

## By this, a side bar is opened. At there, select “API & Services” -> “Library”. After this, follow the below steps:

1. Click “NEW PROJECT” and input the “Project Name”.
2. Click “CREATE” and open the created project.
3. Click “Enable APIs and get credentials like keys”.
4. Go to “Library”
5. Input “Drive API” in “Search for APIs & Services”.
6. Click “Google Drive API” and click “ENABLE”.

## Generating 0Auth2.0 credentials:

1. Follow Enable Drive API section.
2. Open google console.
3. Click on “Credentials”.
4. Click “Create credentials” and select oauth client id.
5. Select Application type “Desktop app” or “other”. 
6. Provide name for the new credentials. ( anything ). This would provide a new Client ID and Client Secret.
7. Download your credentials.json by clicking on the download button.

## You need Access token which can be generated from https://developers.google.com/oauthplayground/

1. Scroll down to Drive API v3. Click on it.

![ezgif-5-a9dd4c19cd](https://user-images.githubusercontent.com/33455151/169865541-92e4647a-2242-4cb6-9a0e-27e12da38d82.jpg)

2. Click on https://www.googleapis.com/auth/drive. And click on Authorize APIs on the bottom left corner.
![ezgif-5-4b72013d40](https://user-images.githubusercontent.com/33455151/169865261-6a781af9-7969-47ef-b645-167eea7a8bc0.jpg)

3. Choose the account which has generated 0Auth2.0 credentials and click on continue.
![tets](https://user-images.githubusercontent.com/33455151/169866428-bf7c9d9e-1fe9-41d2-a102-d5a4e1fbfdd7.png)
![wow](https://user-images.githubusercontent.com/33455151/169866624-104b7fc2-5ffd-4fd2-acab-8565a4d8c4ab.png)

4. Click on the Exchange authorization code for tokens on left side. And copy the access token rom right side.
![ezgif-5-0b9d24c72a](https://user-images.githubusercontent.com/33455151/169865415-d20aaecc-bcf8-4ba0-9b16-7d2d8d7d63d5.jpg)
![ezgif-5-e45ecb9e3d](https://user-images.githubusercontent.com/33455151/169865067-4fd732ce-a318-44ab-909f-2db8eb89d93c.jpg)
