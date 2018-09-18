# import pandas as pd
#
# data = pd.read_csv('ch06/ex1.csv')
# with open('test.txt','a+') as f:
#     for line in data.values:
#         f.write((str(line[0])+'\t'+str(line[1])+'\t'+
#                  str(line[2])+'\t'+str(line[3])+'\t'+str(line[4])+'\n'))
#         #这个是一行中比较少的情况，举得例子只有5列，所以我这么写的，如果列过多则自己处理下吧。