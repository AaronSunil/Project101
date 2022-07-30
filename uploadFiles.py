import os
import dropbox

class TransferData:
    def __init__(self,dropbox):
        return 
    

    def upload_file(self,File_from,File_to):

        dbx = dropbox.Dropbox() 

        for root, dirs, files in os.walk(File_from):
            for name in files:
                print(os.path.join(root, name))
            for path in files:
                print(os.path.join(root, name))

        os.path.join(path) 


def main():

    access_token = 'sl.BMa0RBfGRTJ9W6802GowgWK8Fen0LdkmEZqScxmLAGyrzUfa7zjIFNjxonkzionZgY7xEA3oaDVhh-MhB21Wi4nnRfaeBaWnKs50tCOxzJz-mivVCapHwSEA1Awh9EAvRfF78OI'

    transferData = TransferData(access_token)

    file_from = input('Enter the file to transfer')
    file_to = input('Enter the full path to upload the file to, including name that you wish the file to be called once uploaded')

    transferData.upload_file(file_from,file_to)

    print('File has been moved')

main()
