import sys
import os
import re
import uuid
import urllib

from minio import Minio


def get_image_list(root_dir):
    """获取文件夹及其子文件夹下所有图像文件的列表

    根据文件后缀名，来获取文件夹及其子文件夹下所有的图像文件列表。
    后缀匹配：[.jpeg|.jpg|.png]

    Args:
        root_dir: 根目录

    Returns:
        返回一个包含完整路径名的图像文件 list。

    """

    IMAGE_FILE_EXTENSIONS = 'jpg|jpeg|png'
    image_list = []

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if re.match(f'.*\.(?i:{IMAGE_FILE_EXTENSIONS})$', file) != None:
                image_list.append(os.path.join(root, file))

    return image_list


def upload_image_to_s3(s3_client, bucket, image_list):
    """上传图像文件到 S3 Server

    将image_list中的图像文件，逐一上传到指定的s3_url的指定bucket中。

    Args:
        s3_client: S3 Server 的客户端对象
        bucket: 指定桶，如果不存在则创建它。
        image_list: 图像文件列表

    Returns:
        case_id: 本次上传的唯一标识
        url_list: 访问图像的链接列表

    """

    case_id = str(uuid.uuid1())
    url_list = []

    return case_id, url_list


if __name__ == '__main__':
    # 检查是否指定了案件路径
    if len(sys.argv) == 1:
        print('Usage: batch-submit <批量提交案件所在目录>\n')
        exit(1)

    # 检查指定的目录是否存在
    if not os.path.exists(sys.argv[1]):
        print('error: 目录 "%s" 不存在，请检查目录名是否正确。' % sys.argv[1])
        print('Usage: batch-submit <批量提交案件所在目录>\n')
        exit(1)

    # 列出目标目录下的一级子目录
    root_dir = sys.argv[1]
    sub_dirs = os.listdir(root_dir)

    s3_client = Minio(
        "localhost:9000",
        access_key="minio",
        secret_key="minio123",
        secure=False,
    )

    # 遍历每个子目录
    for sub_dir in sub_dirs:
        # 获取子目录下的所有图像文件列表
        image_list = get_image_list(os.path.join(root_dir, sub_dir))

        # 将图像文件上传到 Minio Server
        case_id, url_list = upload_image_to_s3(s3_client, "temp", image_list)

        # 生成报案
