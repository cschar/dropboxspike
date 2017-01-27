import dropbox
import os

token = os.environ.get('DBX_APP_TOKEN')

dbx = dropbox.Dropbox(token)



for entry in dbx.files_list_folder('').entries:
    print(entry.name)

import ipdb; ipdb.set_trace()
for entry in dbx.files_list_folder('/apple').entries:
    print(entry.name)
    #download files
    dbx.files_download_to_file('/tmp/%s' % entry.path_lower, entry.path_lower)


    #run task

