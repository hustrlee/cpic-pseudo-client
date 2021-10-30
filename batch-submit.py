import sys
import os
import re

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

    # 遍历每个子目录
    for sub_dir in sub_dirs:
        image_list = get_image_list(os.path.join(root_dir, sub_dir))
        print(image_list)
