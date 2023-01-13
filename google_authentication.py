
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

'''
This is a credential validation

######### Google Authentication #########

gauth = GoogleAuth()
######### Try to load saved client credentials

GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = 'credentials/client_secrets.json'
gauth.LoadCredentialsFile("credentials/mycreds.txt")

if gauth.credentials is None:
    # Authenticate if they're not there
    # gauth.LocalWebserverAuth() # <-- WebApp approval
    gauth.CommandLineAuth()  # <-- Command Line Approva

elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()

else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("credentials/mycreds.txt")
drive = GoogleDrive(gauth)
