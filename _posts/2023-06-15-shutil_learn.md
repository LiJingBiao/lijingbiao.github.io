---
layout: post
title: shutil模块使用
date: 2023-06-15
tags: python
---

```
# f = open("dict_learn.py",'r',encoding = 'UTF-8')

# print(f)


# content = f.read(200)
# print(content)

# content = f.readlines()

# print(content)

# for line in f:
#     print(line)


# f.close()


# with open("learn1.py","r",encoding = 'UTF-8') as f:
#     count  = f.read().count("print")
#     print(count)
#     # for line in f:
#     #     print(line)


# with open("test.txt",'w',encoding = "UTF-8") as f:
#     f.write("这是测试内容")
#     f.flush()


import os
import shutil

# 定义一个函数，递归地删除一个目录及其子目录下的所有文件
def delete_all_files(dir):
    # 遍历目录中的所有文件和子目录
    for item in os.listdir(dir):
        # 拼接完整的路径
        path = os.path.join(dir, item)
        # 如果是文件，就删除它
        if os.path.isfile(path):
            os.remove(path)
            print(f"Deleted file: {path}")
        # 如果是子目录，就递归地调用函数删除它
        elif os.path.isdir(path):
            delete_all_files(path)
            # 删除空的子目录
            os.rmdir(path)
            print(f"Deleted directory: {path}")

def delete_all_files2():
    # 获取当前目录
    current_dir = os.getcwd()
    # 调用函数删除当前目录及其子目录下的所有文件
    delete_all_files(current_dir)
    # 删除空的当前目录（如果需要的话）
    os.rmdir(current_dir)
    print(f"Deleted directory: {current_dir}")
    # 获取当前目录
    current_dir = os.getcwd()
    # 使用os.walk()函数遍历当前目录及其子目录
    for root, dirs, files in os.walk(current_dir, topdown=False):
        # 遍历每个文件，删除它
        for file in files:
            path = os.path.join(root, file)
            os.remove(path)
            print(f"Deleted file: {path}")
        # 遍历每个子目录，使用shutil.rmtree()函数删除它
        for dir in dirs:
            path = os.path.join(root, dir)
            shutil.rmtree(path)
            print(f"Deleted directory: {path}")
    # 删除空的当前目录（如果需要的话）
    os.rmdir(current_dir)
    print(f"Deleted directory: {current_dir}")

"""
shutil是一个Python的标准库模块，它提供了一些高级的文件操作函数，例如复制、移动、删除文件和目录12。它可以帮助你自动化一些文件处理的任务，比如在没有实际处理的情况下，打开、读取、写入和关闭文件3。它和os模块有些类似，但是os模块主要处理单个文件，而shutil模块主要处理文件集合4。

shutil模块中的一些常用函数有：

shutil.copy()：复制文件内容（不包括元数据）到另一个文件或目录。
shutil.copy2()：复制文件内容和元数据到另一个文件或目录。
shutil.copyfile()：复制文件内容（不包括元数据）到另一个文件。
shutil.copyfileobj()：复制类似文件对象的内容到另一个类似文件对象。
shutil.copytree()：复制整个目录树到另一个位置。
shutil.move()：移动文件或目录到另一个位置。
shutil.rmtree()：删除整个目录树。
shutil.disk_usage()：返回给定路径的磁盘使用情况。
shutil.make_archive()：创建压缩归档文件（如zip或tar）。
shutil.unpack_archive()：解压缩归档文件（如zip或tar）。
更多关于shutil模块的信息，你可以参考官方文档1或其他在线教程234。

# 复制file1.txt到file1_copy.txt
shutil.copy("test/file1.txt", "test/file1_copy.txt")

# 复制file2.py到sub目录下
shutil.copy("test/file2.py", "test/sub")

# 复制sub目录及其内容到test_copy目录下
shutil.copytree("test/sub", "test/test_copy")

# 移动file3.jpg到sub目录下
shutil.move("test/file3.jpg", "test/sub")

# 删除file1_copy.txt
os.remove("test/file1_copy.txt")

# 创建一个名为test.zip的压缩归档文件，包含test目录及其内容
shutil.make_archive("test", "zip", "test")

# 解压缩test.zip到test_unzip目录下
shutil.unpack_archive("test.zip", "test_unzip")
"""

```
