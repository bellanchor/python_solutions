#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 解决windows下生成的zip文件在linux下解压后全部变为乱码的问题
# from: https://www.zhihu.com/question/20523036

import os
import sys
import zipfile

file=zipfile.ZipFile(sys.argv[1],"r");
for name in file.namelist():
    utf8name=name.decode('gbk')
    pathname = os.path.dirname(utf8name)
    if not os.path.exists(pathname) and pathname!= "":
        os.makedirs(pathname)
    data = file.read(name)
    if not os.path.exists(utf8name):
        fo = open(utf8name, "w")
        fo.write(data)
        fo.close

file.close()
