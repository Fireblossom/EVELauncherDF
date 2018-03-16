#!/usr/bin/env python2
from __future__ import print_function
import contextlib
import os
import extract
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def Depack(version):
    datFilename = 'RepairData_' + version + '.dat'
    extract.ExtractFile(datFilename)

def GetUpdatePack(verison):
    if os.path.isfile('RepairData_' + version + '.dat'):
        print("Update pack is already exists.")
    else:
        url = 'http://cdnupdateeve.tiancity.cn/' + verison + '/RepairData_' + verison + '.dat'
        print("Downloading update pack.")
        r = requests.get(url, stream=True)
        size = int(r.headers['content-length'])
        with contextlib.closing(r) as code:
            with open("RepairData_" + verison + ".dat", "wb") as file:
                accepts = 0
                for data in r.iter_content(chunk_size=2048):
                    accepts += len(data)
                    print(str(accepts) + "/" + str(size), end="\r")
                    file.write(data)

def GetVersion():
    url = 'http://client.eve-online.com.cn/patches/premium_patchinfoSERENITY_inc.txt'
    r = requests.get(url)
    version = r.text[6:13]
    print("Current verison is " + version)
    return version

if __name__=='__main__':
    version = GetVersion()
    GetUpdatePack(version)
    Depack(version)