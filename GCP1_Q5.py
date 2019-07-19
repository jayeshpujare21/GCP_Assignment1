# Imports the Google Cloud client library
from google.cloud import storage


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
		destination_file_name))

def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.delete()
    print('Blob {} deleted.'.format(blob_name))

def copy_blob(bucket_name, blob_name, new_bucket_name, new_blob_name):
    """Copies a blob from one bucket to another with a new name."""
    storage_client = storage.Client()
    source_bucket = storage_client.get_bucket(bucket_name)
    source_blob = source_bucket.blob(blob_name)
    destination_bucket = storage_client.get_bucket(new_bucket_name)

    new_blob = source_bucket.copy_blob(
        source_blob, destination_bucket, new_blob_name)

    print('Blob {} in bucket {} copied to blob {} in bucket {}.'.format(
        source_blob.name, source_bucket.name, new_blob.name,
        destination_bucket.name))

def move_blob(bucket_name, blob_name, new_bucket_name, new_blob_name):
	copy_blob(bucket_name, blob_name, new_bucket_name, new_blob_name)
	delete_blob(bucket_name, blob_name)
	print('Moved')

def main():
	#upload_blob('jaygcp-bucket','gcp1_4.txt','gcp1_4.txt')
	#download_blob('jaygcp-bucket','dest_file.txt','download_t.txt')
	#delete_blob('jaygcp-bucket','gcp1_4.txt')
	#copy_blob('jaygcp-bucket','dest_file.txt','jaygcp-bucket','dest2.txt')
	move_blob('jaygcp-bucket','dest2.txt','b-yr-assess1','moved.txt')
if __name__ == '__main__':
	main()