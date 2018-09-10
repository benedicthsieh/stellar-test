import boto3
import botocore
import scrub_dob_util
import os


# https://docs.google.com/document/d/157bpzroV13dzR5NIO_dx-qihAlYHrzVdjoSXozAVyKE/edit#
# before running this, run 'aws configure' with the credentials in the doc.
BUCKET_NAME = 'stellar.health.code.test'
KEY = 'patients.log'
LOCAL_FILE_NAME = 'local_patients.log'
SCRUBBED_FILE_NAME = 'local_patients.scrubbed.log'
HEADER_LENGTH = 2

# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html
def download_file():
    s3 = boto3.resource('s3')

    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, LOCAL_FILE_NAME)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

def write_scrubbed_file():
    f1 = open(LOCAL_FILE_NAME, 'r')
    try:
        os.remove(SCRUBBED_FILE_NAME)
    except:
        pass
    f2 = open(SCRUBBED_FILE_NAME, 'w')
    line_i = 0
    for line in f1:
        if line_i < HEADER_LENGTH:
            f2.write(line)
        else:
            f2.write(scrub_dob_util.scrub_line(line) + '\n')
        line_i += 1
    f1.close()
    f2.close()

# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html
# https://stackoverflow.com/questions/7585307/how-to-correct-typeerror-unicode-objects-must-be-encoded-before-hashing
def upload_scrubbed_file():
    data = open(SCRUBBED_FILE_NAME, 'rb')
    s3 = boto3.resource('s3')
    s3.Bucket(BUCKET_NAME).put_object(Key=KEY, Body=data)

def main():
    #download_file()
    write_scrubbed_file()
    upload_scrubbed_file()

if __name__ == "__main__":
    main()