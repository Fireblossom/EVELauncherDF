#!/usr/bin/env python3
import requests
import hashlib
import sys
import re
import os

def MD5Check(finename, block_size=64 * 1024):
  with open(finename, 'rb') as f:
    md5 = hashlib.md5()
    while True:
      data = f.read(block_size)
      if not data:
        break
      md5.update(data)
    retmd5 = md5.hexdigest()
    return retmd5

def UpdateGameCache(CachePath):
    file = open('resfileindex.txt')
    lines = len(file.readlines())
    count = 0
    with open('resfileindex.txt') as f:
        for line in f:

            count += 1
            print(str(int((count + 1)/2)) + ' of ' + str(lines), end="\r")
            #print(len(line))
            if len(line) > 1:#qiguai cuowu
                filename = re.split('[,\s]\s*', line)[1].replace('/', '\\')
                filemd5 = re.split(r'[,\s]\s*', line)[2]
                #print(CachePath+filename)
                #print(MD5Check(CachePath+filename))

                if os.path.isfile(CachePath + filename) and MD5Check(CachePath + filename) == filemd5:
                    print('ok', end="\r")
                else:
                    print(re.split('[,\s]\s*', line)[0] + 'need download')
                    url = 'http://res.eve-online.com.cn/' + re.split('[,\s]\s*', line)[1]
                    r = requests.get(url, stream=True)
                    size = int(r.headers['content-length'])
                    with contextlib.closing(r) as code:
                        with open(CachePath + filename, "wb") as file:
                            accepts = 0
                            for data in r.iter_content(chunk_size=2048):
                                accepts += len(data)
                                print(str(accepts) + "/" + str(size), end="\r")
                                file.write(data)

if __name__=='__main__':
    path = sys.argv[1]#Read reg in the future.
    UpdateGameCache(path)#juedui lujing!!
