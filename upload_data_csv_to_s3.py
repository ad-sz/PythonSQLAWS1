import pyodbc
import pandas as pd
import boto3
from global_variables import *
from global_variables import FILENAME_SALES_DATA_CSV, BUCKET_NAME_S3, OBJECT_NAME_SALES_DATA_S3

# create c3 client for communication with AWS s3
s3 = boto3.client('s3')

# upload csv file to AWS s3 (variables saved in global_variables.py)
s3.upload_file(FILENAME_SALES_DATA_CSV, BUCKET_NAME_S3, OBJECT_NAME_SALES_DATA_S3)