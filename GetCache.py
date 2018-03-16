#!/usr/bin/env python3
import requests
import hashlib
import sys
import re
import os

def md5sum(filename):             
    fd = open(filename,"r")  
    fcont = fd.r  
    fd.close()           
    fmd5 = hashlib.md5(fcont)  
    return fmd5.hexdigest()

def UpdateGameCache(CachePath):
    file = open('resfileindex.txt')
    lines = len(file.readlines())
    count = 0
    with open('resfileindex.txt', 'rt') as f:
        for line in f:
            count += 1
            print(str(count) + ' of ' + str(lines), end="\r")
            filename = re.split(r'[,\s]\s*', line)[1]
            filemd5 = re.split(r'[,\s]\s*', line)[2]
            if os.path.isfile(CachePath+filename) and md5sum(CachePath+filename)==filemd5:
                continue
            else:#download


if __name__=='__main__':
    path = sys.argv[1]#Use reg in the future.
    UpdateGameCache(path)#jueduilujing!!
