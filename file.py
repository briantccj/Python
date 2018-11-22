# coding=utf-8
# !/usr/bin/python3

import os
import shutil

file_dir = "C:\\Users\\admin\\Desktop\\test"
os.chdir(file_dir)
shutil.rmtree("sunmi1")                        #删除文件夹
shutil.copytree("sunmi0","sunmi1")            #拷贝文件夹，参数二必须是不存在的新目录