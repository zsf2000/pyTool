# -*- coding: utf-8 -*-

import sys
import logging
import pathlib
import os
from logging import handlers


class Log:
    #日志输出类
    # 日志级别关系映射
    level_relations = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'crit': logging.CRITICAL
}
    def __init__(self,filename,level):
        filename=os.path.join('.',filename)
        self.filename=filename
        self.level=level

    #
    #Debug级别
    #
    def logOut(self):
    # 创建日志对象
     log = logging.getLogger(self.filename)
     global  console_handler
     global  file_handler
    #  这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
     if not log.handlers:
         console_handler = logging.StreamHandler(sys.stdout)
         file_handler = handlers.RotatingFileHandler(filename=self.filename, maxBytes=1*1024*1024*1024, backupCount=1, encoding='utf-8')
    # 设置日志级别
     log.setLevel(self.level_relations.get(self.level))
    # 日志输出格式
     fmt = logging.Formatter('%(asctime)s %(thread)d %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    # 输出到控制台
     console_handler.setFormatter(fmt)
    # 输出到文件
     if not pathlib.Path(self.filename).exists():
        print('error,file doesn`t exist,new a file')
        open(self.filename,'w') 
    # 日志文件按天进行保存，每天一个日志文件
    #file_handler = handlers.TimedRotatingFileHandler(filename=filename, when='D', backupCount=1, encoding='utf-8')
    # 按照大小自动分割日志文件，一旦达到指定的大小重新生成文件

     file_handler.setFormatter(fmt)

     log.addHandler(console_handler)
     log.addHandler(file_handler)
     return log

 









