#-*-coding:utf-8 -*-
# txt轉csv
import csv
with open('file.csv', 'r+') as csvfile:
    spamwriter = csv.writer(csvfile)
    # 读要转换的txt文件，文件每行各词间以@@@字符分隔
    with open('top20_new.txt', 'r+') as filein:
        for line in filein:
            line_list = line.strip('\n').split(',')
            spamwriter.writerow(line_list)