import os
import shutil
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    #initialize dropbox
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        #read as binary file
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

        for root, dirs, files in os.walk(file_from):
            for file_name in files:
                local_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

            with open(local_path, 'rb') as f:
                dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))
    
    def main():
        access_token = 'sl.A5PCzPIYzEfKJpv07BQfPpPldT-aFmT9BAUWIcvTZhIBzQVvCQ5V303dd2hi7uTb2tA4p6E7bNjW13Spxe9nLPsdAn8oPGMe5_Z5WDKK559dhVapbpybKlhL7R-KOk-vsWI9JsI'
        transferData = TransferData(access_token)
        file_from = input("Enter file path here: ")
        file_to = input("Enter the full path to upload it to Dropbox: ")
    
