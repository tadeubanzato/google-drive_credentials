# Google Drive Credentials
This is the best way to do a credential check and validation from Google Drive using python.
Please feel free to iterate, dwonload and use as you want.

All data in the credetial file is fake so do not forget to update and change.

## Quick Explanation
I've been doing a few Python project just for hobby and one of the projects I need to upload a most recent version of a file gneerated by the python script.
I always had major issues with credential validation and refresh of the credentials so instead of having to solve every time an issue happened I tried to build a better version of what was my first iteration of a file transfer scrip to Google Drive.

## How to get the Google Drive credentials
> I do not need to say that you will have to create an account in case you do not have it

1. Enable the Gdrive credential in your Google Cloud page: https://console.cloud.google.com/apis/dashboard
2. Click on the + ENABLE APIS AND SERVICES link on top below the search bar
3. Find the Google Drive API and click on it to enable (should be straight forward but I'll add screenshots later)

#### Once you Enable the GDrive API you will need to generate a credential
1. On the left menu or through this direct link https://console.cloud.google.com/apis/credentials you get to where the work needs to be done.
2. Click on +CREATE CREDENTIALS on the upper part of the screen below the search bar
4. Once you click to create the credentials you need to select OAuth client ID - https://console.cloud.google.com/apis/credentials/oauthclient
5. Select Destop App in the dropdown and give a name to your app
6. This is essentially it. you now have 0Auth client created
7. At this point you can download the JSON file from the link shown on the light box. - Do not share this information or data to anyone.

The file will look something like this:
```json
{
   "installed":{
      "client_id":"CLIENT-ID",
      "project_id":"PROJECT-ID",
      "auth_uri":"https://accounts.google.com/o/oauth2/auth",
      "token_uri":"https://oauth2.googleapis.com/token",
      "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
      "client_secret":"CLIENT-SECRET",
      "redirect_uris":[
         "http://localhost"
      ]
   }
}
```

# Python 0Auth GDrive

The script use the PyDrive library: https://pypi.org/project/PyDrive/

You should be able to install it by runing `pip3 install PyDrive `

Once the library is installed here is the script `google_authentication.py`
```python
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

## Start Google Authentication
gauth = GoogleAuth()

# Load JSON credentials downloaded from Google
GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = 'credentials/client_secrets.json'
# Try to use the credential .txt generated at the first 0Auth approval
gauth.LoadCredentialsFile("credentials/mycreds.txt")

# If the app was not yet authenticated it will ask to get the authentication from Google
if gauth.credentials is None:
    # Authenticate if they're not there
    # gauth.LocalWebserverAuth() # <-- WebApp approval
    gauth.CommandLineAuth()  # <-- Command Line Approva

# If credential has expired refresh
elif gauth.access_token_expired:
    gauth.Refresh()

# Initialize the saved creds
else:
    gauth.Authorize()

# Save current credentials into a TXT file for the future
gauth.SaveCredentialsFile("credentials/mycreds.txt")
drive = GoogleDrive(gauth)
```
## After Authentication
After the connection and authentication is done you can run the example script below to list all files
```python
## Example: List all files in the drive
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))
```

More references on PyDrive documentation:
https://pythonhosted.org/PyDrive/index.html
