import csv   # 導入csv包
#! /usr/bin/env python
# -*- coding: utf-8 -*-

# LIMIT=600000
LIMIT=3
file_count=0
url_list=[]
# 讀取本地CSV文檔
csv_file=csv.reader(open("file2.csv",'r+',newline=''))
# 循環輸出每一行信息
for stu in csv_file:
    # print(stu)
    url_list.append(stu)
    print(url_list)
    if len(url_list)<LIMIT:
        continue

    file_name=str(file_count)+".csv"
    with open(file_name,'w',newline='') as file:
        for url in url_list:
            writer=csv.writer(file)
            # file.write(url)
        # file.writerows(url_list[-1].strip())
        writer.writerows(url_list)
        url_list=[]
        file_count+=1
if url_list:
    file_name=str(file_count)+".csv"
    with open(file_name,'w+') as file:
        for url in url_list:
            writer=csv.writer(file)



print('done test')