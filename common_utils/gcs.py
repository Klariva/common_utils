from google.cloud import storage, storage_control_v2

def download_from_bucket(bucket, blob_path, temp_path):
    # download csv from gcs
    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.blob(blob_path)
    blob.download_to_filename(temp_path)

def upload_to_bucket(bucket, blob_path, f):
    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.blob(blob_path)
    if not blob.exists():
        blob.upload_from_file(f, rewind=True)
        print(f"Uploaded: {blob_path}")
    else:
        print(f"File already exists: {blob_path}")

def create_folder(bucket, folder_name):
    storage_control_client = storage_control_v2.StorageControlClient()
    project_path = storage_control_client.common_project_path("_")
    bucket_path = f"{project_path}/buckets/{bucket}"

    request = storage_control_v2.CreateFolderRequest(
        parent=bucket_path,
        folder_id=folder_name,
    )
    response = storage_control_client.create_folder(request=request)
    print(f"Created folder: {response.name}")

def get_file_by_prefix(bucket, prefix):
    client = storage.Client()
    bucket = client.bucket(bucket)
    # returns all matching files
    blobs = list(bucket.list_blobs(prefix=prefix))
    if not blobs:
        raise FileNotFoundError(f"No file found in bucket '{bucket}' with prefix '{prefix}'")
    # return the first match
    return blobs[0].name

def folder_or_file_exists(bucket, object_name):
    client = storage.Client()
    bucket = client.bucket(bucket)
    blobs = list(bucket.list_blobs(prefix=object_name))
    if not blobs:
        return False
    else:
        return True
