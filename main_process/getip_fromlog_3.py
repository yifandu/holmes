#-*- coding:utf-8 -*-
# try pull request

import re,time
def mail_log(file_path):
        global count
        log=open(file_path,'r')
        C=r'(?<=[\s])(?:\d{1,3}\.){3}\d{1,3}(?=[\s])'
        find=re.compile(C)
        count={}
        for i in log:
            for ip in find.findall(i):
                count[ip]=count.get(ip,0)+1
if __name__ == '__main__':

        mail_log(r'access.log')
        R=count.items()
        for i in R:
            if i[1]>0: #提取出现次数大于0的IP
                print i[0]


