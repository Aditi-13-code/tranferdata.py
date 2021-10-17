import dropbox 
os.walk( top[, topdown=True[, onerror=None[, followlinks=False]]])

class TransferData: 

import os
    path = "/home"
    print(os.path.join(path, "User/Desktop", "file.txt"))
    path = "User/Documents"
    print(os.path.join(path, "/home", "file.txt"))
    path = "/User"

    print(os.path.join(path, "Downloads", "file.txt", "/home"))


    path = "/home"

print(os.path.join(path, "User/Public/", "Documents", ""))



    for root, dirs, files in os.walk(file_from):
        def __init__(self, access_token):
            self.access_token=access_token

        def upload_file(self,file_from,file_to):
            dbx = dropbox.Dropbox (self.access_token)

            f = open(file_from,'rb')
            dbx.files_upload(f.read(),file_to)
    
        def main():
            access_token = 'sl.A6T2qQtAhOtIl1QbXJVpiOXBCFf4zbJmx5VDW_TfCQ8EyLS3g9s5DtHDYNWCmbB5NUOmkSJPgBUQRyD4QbBjXuYHttTUzJILaHAK3GgDiBMJnO0rRrBTpqRnwaGwT51BStkN3-4'
            transferData = TransferData(access_token)

            file_from =input("Enter File's Path That You Want To Transfer:")
            file_to =input("Enter The Full Path To Upload To Dropbox:")

        transferData.upload_file(file_from,file_to)
        print("Files Has Benn Moved")

    main()
