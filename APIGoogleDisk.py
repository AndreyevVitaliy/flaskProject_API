from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload,MediaFileUpload
from googleapiclient.discovery import build
import pprint
import io
import os.path

pp = pprint.PrettyPrinter(indent=4)
#
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = '/Users/vitaliy/Desktop/Python/APIGoogleDiskTest/caramel-abode-344609-de6440843dc4.json'

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)
#
# results = service.files().list(pageSize=10,
#                                fields="nextPageToken, files(id, name, mimeType)").execute()
# nextPageToken = results.get('nextPageToken')
# while nextPageToken:
#         nextPage = service.files().list(pageSize=10,
#                                         fields="nextPageToken, files(id, name, mimeType, parents)",
#                                         pageToken=nextPageToken).execute()
#         nextPageToken = nextPage.get('nextPageToken')
#         results['files'] = results['files'] + nextPage['files']
# pp.pprint(results.get('files'))

file_id = '1Der2vXRQDraJCSSucgVVzWLPO0B2o8fQ'
request = service.files().get_media(fileId=file_id)
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print("Download %d%%." % int(status.progress() * 100))

