from abc import ABC, abstractmethod

class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self, filename):
        pass

    @abstractmethod
    def download_file(self, filename):
        pass

    @abstractmethod
    def delete_file(self, filename):
        pass

class S3Storage(CloudStorage):
    def upload_file(self, filename):
        print(f'Amazon S3: Uploaded {filename} to s3://my-bucket/')

    def download_file(self, filename):
        print(f'Amazon S3: Downloaded {filename} from s3://my-bucket/')

    def delete_file(self, filename):
        print(f'Amazon S3: Deleted {filename} from s3://my-bucket/')

class GoogleDriveStorage(CloudStorage):
    def upload_file(self, filename):
        print(f'Google Drive: Uploaded {filename} to root drive folder')

    def download_file(self, filename):
        print(f'Google Drive: Downloaded {filename} stream')

    def delete_file(self, filename):
        print(f'Google Drive: Moved {filename} to trash')

class AzureBlobStorage(CloudStorage):
    def upload_file(self, filename):
        print(f'Azure Blob: Uploaded {filename} to container documents')

    def download_file(self, filename):
        print(f'Azure Blob: Downloaded {filename} blob block')

    def delete_file(self, filename):
        print(f'Azure Blob: Deleted {filename} blob')

services = [S3Storage(), GoogleDriveStorage(), AzureBlobStorage()]
for s in services:
    s.upload_file('report.pdf')
    s.download_file('report.pdf')
    s.delete_file('report.pdf')
    print()
