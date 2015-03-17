#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup, find_packages
import sys, os
"""
打包的用的setup必须引入
"""

VERSION = '0.1.2'


setup(
      name='nyancat', # 文件名
      version=VERSION, # 版本(每次更新上传Pypi需要修改)
      description="nyancat in your terminal based on Python!",
      long_description='', # 放README.md文件,方便在Pypi页展示
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python nyancat terminal', # 关键字
      author='taizilongxu', # 用户名
      author_email='468137306@qq.com', # 邮箱
      url='https://github.com/taizilongxu/nyancat', # github上的地址,别的地址也可以
      license='MIT', # 遵循的协议
      packages=['nyancat'], # 发布的包名
      include_package_data=True,
      zip_safe=True,
      install_requires=[
      ], # 满足的依赖
      entry_points={
        'console_scripts':[
            'nyancat = nyancat.nyancat:main'
        ]
      },
)
