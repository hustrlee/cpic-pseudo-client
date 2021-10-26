import sys
import os

if len(sys.argv) == 1:
    print("Usage: batch-submit <批量提交案件所在目录>\n")
    exit(1)

# 检查指定的目录是否存在
if not os.path.exists(sys.argv[1]):
    print("error: 目录 '%s' 不存在，请检查目录名是否正确。\n" % sys.argv[1])
    print("Usage: batch-submit <批量提交案件所在目录>\n")
    exit(1)

# 列出目标目录下的一级子目录，目录名作为案件号
root_dir = sys.argv[1]
sub_dirs = os.listdir(root_dir)
