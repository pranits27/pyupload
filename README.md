# pyupload
Uploading file on gdrive using Python

First of all you need to enable Google drive API:

1. Log into google developer console at https://console.cloud.google.com/apis/dashboard.
2. Click select project at the right side of “Google Cloud Platform” of upper left of window.
3. If you cannot see the project, please try to access to https://console.cloud.google.com/cloud-resource-manager.

You can also create new project at there. When you create a new project there, please click the left of “Google Cloud Platform”. You can see it like 3 horizontal lines.

By this, a side bar is opened. At there, select “API & Services” -> “Library”. After this, follow the below steps:

1. Click “NEW PROJECT” and input the “Project Name”.
2. Click “CREATE” and open the created project.
3. Click “Enable APIs and get credentials like keys”.
4. Go to “Library”
5. Input “Drive API” in “Search for APIs & Services”.
6. Click “Google Drive API” and click “ENABLE”.

Generating 0Auth2.0 credentials:

1. Follow Enable Drive API section.
2. Open google console.
3. Click on “Credentials”.
4. Click “Create credentials” and select oauth client id.
5. Select Application type “Desktop app” or “other”. 
6. Provide name for the new credentials. ( anything ). This would provide a new Client ID and Client Secret.
7. Download your credentials.json by clicking on the download button.

You need Access token which can be generated from https://developers.google.com/oauthplayground/

1. Scroll down to Drive API v3. Click on it.
2. Click on https://www.googleapis.com/auth/drive. And click on Authorize APIs on the bottom left corner.
3. Choose the account which has generated 0Auth2.0 credentials and click on continue.
4. Click on the Exchange authorization code for tokens on left side. And copy the access token rom right side.