import logging
import sys
import os
import re
import uuid
import time
from hashlib import md5
import json
from urllib import request

from aes_ecb import AESCipher
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


def upload_image_to_s3(s3_client, bucket, src_dir, image_list):
    """上传图像文件到 S3 Server

    将image_list中的图像文件，逐一上传到指定的s3_url的指定bucket中。

    Args:
        s3_client: S3 Server 的客户端对象
        bucket: 指定桶，如果桶不存在则创建它
        src_dir: 图像文件的源目录
        image_list: 图像文件列表

    Returns:
        case_id: 本次上传的唯一标识
        url_list: 访问图像的链接列表

    """

    case_id = str(uuid.uuid1())
    url_list = []

    # 检查桶是否存在
    if not s3_client.bucket_exists(bucket):
        s3_client.make_bucket(bucket)

    print(f'将 "{src_dir}" 上载到 "{bucket}/{case_id}/" : ', end='')
    print('0%', end='')
    for i in range(len(image_list)):
        # 将图像文件存储到桶
        print('...', end='', flush=True)
        image_path, image_filename = os.path.split(image_list[i])
        s3_client.fput_object(
            bucket,
            f'{case_id}/{image_filename}',
            image_list[i],
        )
        print(f'{int((i+1)/len(image_list)*100)}%', end='', flush=True)

        # 获取图像文件分享链接
        url = s3_client.get_presigned_url(
            'GET',
            bucket,
            f'{case_id}/{image_filename}',
        )
        url_list.append({"id": str(i), "name": image_filename, "url": url})
    print('')

    return case_id, url_list


if __name__ == '__main__':
    # 检查是否指定了案件路径
    if len(sys.argv) < 4:
        print('Usage: batch-submit <批量提交案件所在目录> <S3 地址> <createCase 地址>\n')
        print('Example: batch-submit ./data accesskey:secretkey@localhost:9000 localhost:3001')  # noqa
        sys.exit(1)

    # 检查指定的目录是否存在
    if not os.path.exists(sys.argv[1]):
        print('error: 目录 "%s" 不存在，请检查目录名是否正确。' % sys.argv[1])
        sys.exit(1)

    # 扫描目标目录下的一级子目录
    root_dir = sys.argv[1]
    sub_dirs = os.listdir(root_dir)
    print('在目录 "%s" 中共扫描到 %s 个子目录' % (root_dir, len(sub_dirs)))

    s3_params = re.split(r'[:|@]', sys.argv[2])
    access_key = s3_params[0]
    secret_key = s3_params[1]
    endpoint = s3_params[2] + ':' + s3_params[3]
    s3_client = Minio(
        endpoint=endpoint,
        access_key=access_key,
        secret_key=secret_key,
        secure=False,
    )

    # 检查 temp 桶是否存在
    try:
        if not s3_client.bucket_exists('temp'):
            s3_client.make_bucket('temp')
    except Exception:
        print('无法连接到 S3 服务器：%s:%s@%s' % (access_key, secret_key, endpoint))
        sys.exit(1)

    # 分配给广东太保的用户参数
    gdtb = {
        "custid": "21",
        "appkey": "asdfghjkl",
        "secretkey": "dwsuhfci",
        "salt": "gdtb",
    }

    # 遍历每个子目录
    for sub_dir in sub_dirs:
        # 获取子目录下的所有图像文件列表
        image_list = get_image_list(os.path.join(root_dir, sub_dir))

        # 将图像文件上传到 Minio Server
        case_id, url_list = upload_image_to_s3(
            s3_client,
            "temp",
            sub_dir,
            image_list,
        )

        # Payload
        token = {
            "appkey": gdtb["appkey"],
            "images": url_list,
            "insurecode": "130701199310302288",
            "insurename": "张三",
            "registno": sub_dir,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            "weight": "3",
            "zmark": "",
        }

        case_uuid = str(uuid.uuid1())

        # 生成签名 sign
        sign_md5 = md5()
        sign_md5.update(token["appkey"].encode("utf-8"))
        sign_md5.update(token["registno"].encode("utf-8"))
        sign_md5.update(token["timestamp"].encode("utf-8"))
        sign_md5.update(case_uuid.encode("utf-8"))
        sign_md5.update(gdtb["secretkey"].encode("utf-8"))
        token["sign"] = sign_md5.hexdigest()

        # 对 Payload 进行加密
        token_cipher = AESCipher(gdtb["salt"]).encrypt(json.dumps(token))

        # POST /api/createCase
        host = sys.argv[3] or "localhost:3001"
        request_body = json.dumps({
            "custid": gdtb["custid"],
            "uuid": case_uuid,
            "token": token_cipher,
            "withCaseInfoInReturn": False
        })
        headers = {"content-type": "application/json"}
        req = request.Request(
            url="http://%s/v1/createCase" % host,
            headers=headers,
            data=request_body.encode("utf-8")
        )

        try:
            res = request.urlopen(req)
            print(res.read().decode("utf-8"))
        except Exception as e:
            print('无法连接到接口服务器：%s' % host)
            sys.exit(1)
