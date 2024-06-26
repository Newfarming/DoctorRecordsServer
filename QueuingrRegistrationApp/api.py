import pymysql


def get_mz_queue_data(paramObj):
    try:
        # connect = pymysql.connect(host='192.168.214.244',
        #                           user='root',
        #                           password="Cent!@#890",
        #                           db='db_test',
        #                           charset='utf8')
        connect = pymysql.connect(host='192.168.111.101',
                                  user='qeasy',
                                  password="qeasy",
                                  db='SmartQueue',
                                  charset='utf8')
        cr = connect.cursor()
        sql1 = ''
        if paramObj['科室名称']:
            sql1 = """ select * from MZ_Queue where (科室名称 like '%""" + paramObj['科室名称'] + """%' )"""
        elif paramObj['门诊号']:
            sql1 = """ select * from MZ_Queue where (门诊号 like '%""" + paramObj['门诊号'] + """%' )"""
        elif paramObj['患者姓名']:
            sql1 = """ select * from MZ_Queue where (患者姓名 like '%""" + paramObj['患者姓名'] + """%' )"""
        elif paramObj['医生姓名']:
            sql1 = """ select * from MZ_Queue where (医生姓名 like '%""" + paramObj['医生姓名'] + """%' )"""
        elif paramObj['电话']:
            sql1 = """ select * from MZ_Queue where (电话 like '%""" + paramObj['电话'] + """%' )"""
        else:
            sql1 = """ select * from MZ_Queue"""

        cr.execute(sql1)
        bi_data = cr.fetchall()
        cr.close()
        connect.close()
        rs_ret = bi_data
        return rs_ret
    except Exception as e:
        print('获取排队叫号列表报错')
        print(e)