import json

import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir='C:\instantclient_21_9')
#conn = cx_Oracle.connect("cognizant/zan12coi3gn@192.168.215.39:1521/SDMAEUAT")
connection = cx_Oracle.connect(user="cognizant", password="zan12coi3gn",
                               dsn="192.168.215.39:1521/SDMAEUAT",
                               encoding="UTF-8")
cursor = connection.cursor()
with open("C:/Users/anam.kumar/PycharmProjects/First/TALABAT_ADP_ALha_KArte/SucessOrderResponse.json" , 'r') as f:
    ntfreetexts=json.load(f)
for data in ntfreetexts:
    exid=data.get('External ID')
    print(exid)
    cursor.execute(f"SELECT Ordr_Status, Ordr_Id FROM Callcenter16.Cc_Order WHERE ORDR_EXTERNALID IN ('{exid}') ")
    row = cursor.fetchone()
    print(row[0])
connection.close()