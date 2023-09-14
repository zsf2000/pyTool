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
        sql = "select * from B6.T_material_ANALYSIS where analysisid=2"
        stmt = ibm_db.exec_immediate(self.conn, sql)   #执行SQL
        result = ibm_db.fetch_assoc(stmt)    #一行一行的执行
        while (result):
            print(result["VALUE"])
            result = ibm_db.fetch_assoc(stmt)
       except:
            log2.debug("sqlerro:",ibm_db.stmt_error)
            log2.debug("sqlerro:",ibm_db.stmt_errormsg)
            ibm_db.close(self.conn)
    ###############################插入料仓数据#######################################
    #函数名：
    #创建时间：
    #描述：
    ##################################################################################
    def InsertBunker(self,SinterLevel_Dict):
        maxID=1
        #self.connect()
        try:
            sql = "select max(ID) as ID from BGRAW.T_TEST "
            print(self.conn)
            stmt = ibm_db.exec_immediate(self.conn, sql)   #执行SQL
            result = ibm_db.fetch_assoc(stmt)    #一行一行的执行
            while (result):
                print("料仓最大ID",result["ID"])
                maxID=result["ID"]
                result = ibm_db.fetch_assoc(stmt)
        except:
                log2.debug("sqlerro:",ibm_db.stmt_error)
                log2.debug("sqlerro:",ibm_db.stmt_errormsg)
                ibm_db.close(self.conn)
        ##############################
        maxID=int(maxID)+1
     
        try:
                stmt1 = ibm_db.prepare(self.conn, "Insert into BGRAW.T_TEST (ID,NO1,NO2,NO3,NO4,NO5,NO6,NO7) VALUES (?, ?, ?,?,?,?,?,?)") 
                column1_value = maxID 
                column2_value   = SinterLevel_Dict[1]
                column3_value   = SinterLevel_Dict[2]
                column4_value 	= SinterLevel_Dict[3]
                column5_value 	= SinterLevel_Dict[4]
                column6_value 	= SinterLevel_Dict[5]
                column7_value 	= SinterLevel_Dict[6]
                column8_value 	= SinterLevel_Dict[7]

                ibm_db.execute(stmt1, (column1_value, column2_value, column3_value,column4_value,column5_value,column6_value,column7_value,column8_value))
        except Exception as e:
                log2.debug(f"SQL Error: {str(e)}")
                log2.debug("sqlerro:",ibm_db.stmt_errormsg)
                ibm_db.close(self.conn)
    ###############################插入结果数据#######################################
    #函数名：InsertResultTable
    #创建时间：
    #描述：
    ##################################################################################
    def InsertResultTable(self,t1,t2,t3):
        print("InsertResultTable")

        nowTime=datetime.datetime.now()
        InBFTime=(nowTime+datetime.timedelta(minutes=(t1+t2))).strftime("%Y-%m-%d %H:%M:%S")
        print("111",InBFTime)
        InBunkerTime=(nowTime+datetime.timedelta(minutes=(t1))).strftime("%Y-%m-%d %H:%M:%S")
        print("222",InBunkerTime)
        nowTime=nowTime.strftime("%Y-%m-%d %H:%M:%S")
        for i in range(1,8):
            try:
                sql = f"INSERT INTO BGRAW.T_ADS_RAW_ABNOR_SINTER_BF1(\
                        BUNKERNO\
                        ,SAMPLETIME\
                        ,BRANDCODE\
                         ,ANALYSISID\
                         ,IN_BUNKERTIME\
                         ,IN_BFTIME\
                         ,ABCOMPONENT\
                         ,ABVALUE\
                         ,STANDARDVALUE\
                         ,ABFLAG\
                         ) VALUES\
                         ({i},'{nowTime}','SJK-1','999','{InBunkerTime}','{InBFTime}','TFE',40,50,1)\
                                            "
                print(sql)
                stmt = ibm_db.exec_immediate(self.conn, sql)   #执行SQL
                log2.debug("插入成功")
            except:
                log2.debug("sqlerro:",ibm_db.stmt_error)
                log2.debug("sqlerro:",ibm_db.stmt_errormsg)
                ibm_db.close(self.conn)


    #断开连接
    def disconnect(self):
        ibm_db.close(self.conn)
        log2.debug("disconnect db2 connection")
        print("disconnect db2 connection")

#conn_str="DATABASE=BF;HOSTNAME=10.25.104.34;PORT=50000;PROTOCOL=TCPIP;UID=bf;PWD=bf;"
#bfDB=PyDB2(conn_str)
#bfDB.connect()
#SinterLevel_Dict={}
#for i in range(1,9):
#    SinterLevel_Dict[i]=random.uniform(0.5,0.9)
#bfDB.InsertBunker(SinterLevel_Dict)