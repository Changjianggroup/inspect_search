from flask import Flask
from flask import request, jsonify, make_response
import pymysql
import datetime
from flask_cors import cross_origin
app = Flask(__name__)

mysql_host = '192.168.1.8'
mysql_port = 3306
mysql_db = 'inspect'
mysql_table = 'inspect_record'
mysql_username = 'root'
mysql_password = '123456'

def api_select_inspect_info_from_mysql(begin=None, end=None):
    conn = pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_username, password=mysql_password)
    conn.autocommit(1)
    cursor = conn.cursor()
    if begin and end:
        sql = f"SELECT * FROM {mysql_db}.{mysql_table} where `date`>= " \
          f"'{begin}' and `date`<= '{end}' ORDER BY `date` DESC"
        print(sql)
    else:
        sql = f"SELECT * FROM {mysql_db}.{mysql_table} ORDER BY `date` DESC"
    cursor.execute(sql)
    desc = cursor.description
    data_dict_list = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
    for item in data_dict_list:
        item['date'] = item['date'].strftime('%Y-%m-%d')
    return data_dict_list

@app.route('/inspect/list',methods=['GET'])
@cross_origin(supports_credentials=True)
def list_inspect_info():
    begin = request.args.get("begin")
    end = request.args.get("end")
    page = request.args.get("page")
    page_size = request.args.get("page_size")
    if begin =='' or end == '':
        info_list = api_select_inspect_info_from_mysql()
    else:
        info_list = api_select_inspect_info_from_mysql(begin, end)
    res_dict = dict()
    count = len(info_list)
    limit = int(page_size)
    offset = (int(page) - 1) * int(page_size)
    data_list = list()
    min = offset
    max = offset + limit
    if max > count:
        max = count
    for i in range(min, max):
        print(i)
        #print(info_list[i])
        data_list.append(info_list[i])
    res_dict['data'] = data_list
    res_dict['count'] = count
    response = make_response(jsonify(res_dict))
    return response

if __name__ == '__main__':

    app.run(port=8000, debug=True)

