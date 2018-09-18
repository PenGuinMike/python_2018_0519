#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import csv

# 初始化編碼
# csv.reload(sys)
# sys.setdefaultencoding('utf-8')

# 讀取本地csv檔案
csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'csv','file.csv')
csv_reader = csv.reader(open('file.csv','r+'))
# csv_reader.next()
i=j=1
for row in csv_reader:
    if i%11==0:
        print ("CSV文件source%s已生成成功") % j
        j+=1
    # 寫入csv
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'csv','source'+str(j)+'.csv')
    csv_file = csv.file('file.csv', 'r+')
    csv_write = csv.writer('file.csv')
    # 文件不存在则写入头部
    if os.path.getsize(csv_path)==0:
        csv_write.writerow(['v_products_image','v_products_name_1','v_products_description_1','v_products_price','v_categories_name_1','v_categories_name_2'])
    # 寫入資料
    csv_write.writerow([row[0],row[1],row[2],row[3],row[4],row[5]])
    csv_file.close()
    i+=1
    # 關閉連接