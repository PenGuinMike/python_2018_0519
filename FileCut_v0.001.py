
#! /usr/bin/env python
# -*- coding: utf-8 -*-

LIMIT=5
file_count=0
url_list=[]
with open("piaeye87.txt") as f:
    for line in f:
        url_list.append(line)
        if len(url_list)<LIMIT:
            continue
        file_name=str(file_count)+".txt"
        with open(file_name,'w') as file:
            for url in url_list[:-1]:
                file.write(url)
            file.write(url_list[-1].strip())
            url_list=[]
            file_count+=1
if url_list:
    file_name=str(file_count)+".txt"
    with open(file_name,'w') as file:
        for url in url_list:
            file.write(url)
print('done test')