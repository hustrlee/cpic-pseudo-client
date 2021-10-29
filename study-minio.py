from minio import Minio
from minio.error import S3Error


def main():
    client = Minio(
        "http://localhost:9000",
        access_key="cpic-gd",
        secret_key="cpic-gd-123"
    )
