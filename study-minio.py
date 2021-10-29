from minio import Minio
from minio.error import S3Error


def main():
    client = Minio(
        "localhost:9000",
        access_key="cpic-gd",
        secret_key="cpic-gd-123",
        secure=False
    )
    bucket_name = "cpic"

    if not client.bucket_exists(bucket_name=bucket_name):
        client.make_bucket(bucket_name=bucket_name)

    client.fput_object(
        bucket_name,
        "1.jpeg",
        "gd-medical-bill-sample.jpg"
    )


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error ocurred.", exc)
