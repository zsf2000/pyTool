#-*- encoding:utf-8 -*-
import sys   #reload()之前必须要引入模块
import ibm_db
import logger
#import GlobalDefine
import random
import datetime

#log类定义
OutLogFileName='C:\\Users\\zsf\\Desktop\\pythonTool\\DB2数据库连接\\log.log'
log1=logger.Log(OutLogFileName,'debug')
log2=log1.logOut()

class PyDB2(object):
    #DB2数据库操作类
    def __init__(self,conn_str=''):
        self.conn_str=conn_str
        try:
            global conn
            self.conn = ibm_db.pconnect(self.conn_str, '', '')     
        except:     
            print ("no connection:error code=", ibm_db.conn_error())
            sys.exit(1)#连接失败立刻终止程序
        else:
            print ("The connection was successful")
            log2.debug(self.conn_str+"||The connection was successful")
    

    #DB2连接函数

    def connect(self):
        pass


    #执行单个SQL语句
    def test1(self,ResultID):
        conn = ibm_db.connect("DATABASE=BF;HOSTNAME=10.25.104.34;PORT=50000;PROTOCOL=TCPIP;UID=bf;PWD=bf;", "", "")
        sql = 'select * from B6.T_MATERIAL_TYPE where TYP='+"'A'"
        try:
            stmt = ibm_db.exec_immediate(conn, sql)
            row = ibm_db.fetch_both(stmt)
            while row != False:
                print( "The  CLAS is : ", dictionary["CLAS"])
                row = ibm_db.fetch_assoc(stmt)
        except:
            print("sqlerro:",ibm_db.stmt_error)
            ibm_db.close(conn)
    #
        #测试
        #f'字符串为格式化  {}内可以输入变量
    def test(self,ResultID):
       try:
        sql = f"select * from B6.T_material_ANALYSIS where analysisid={ResultID}"
        print(sql)
        stmt = ibm_db.exec_immediate(self.conn, sql)   #执行SQL
        result = ibm_db.fetch_assoc(stmt)    #一行一行的执行
        while (result):
            print(result["VALUE"])
            result = ibm_db.fetch_assoc(stmt)
       except:
            log2.debug("sqlerro:",ibm_db.stmt_error)
            log2.debug("sqlerro:",ibm_db.stmt_errormsg)
            ibm_db.close(self.conn)



    #断开连接
    def disconnect(self):
        ibm_db.close(self.conn)
        log2.debug("disconnect db2 connection")
        print("disconnect db2 connection")

conn_str="DATABASE=BF;HOSTNAME=10.25.104.34;PORT=50000;PROTOCOL=TCPIP;UID=bf;PWD=bf;"
bfDB=PyDB2(conn_str)
bfDB.connect()
bfDB.test(2)
