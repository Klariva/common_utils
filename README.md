
# Common Utilities

This repository contains utilities used by cloud run jobs to interact with Google Cloud Storage (GCS) and the Postgres database on GCP. It contains methods for interacting with GCS such as methods to upload to buckets, download from buckets, create folders within a bucket, check whether a file or folder exists in a bucket, as well finding files within a bucket with a given file prefix. It also contains methods for establishing a connection to a cloud hosted Postgres instance via psycopg, as well as running sql commands against a Postgres instance.




## gcs.py

This file contains the following methods: download_from_bucket, upload_to_bucket, create_folder, get_file_by_prefix, folder_or_file_exists


## db.py
This file contains two methods, getconn() which establishes a connection to the database and returns a psycopg Connection object, and run_sql() which runs a given sql command against the database.
## Installation
This package can be installed by running the following:
```pip install git+https://github.com/Klariva/common_utils.git```