#!/usr/bin/env python

def findIMEI(imei):
    """Tries to find an IMEI in the dict"""
    if imei in myDict.keys():
       print "[findIMEI] Found imei"
       return 1
    else:
       print "[findIMEI] Could not find imei!"
       return 0

def storeIMEI(imei):
    print "[findIMEI] imei stored"
    myDict[imei] = 1

def updateIMEI(imei):
    print "[updateIMEI] imei updated"
    cur_value = myDict[imei]
    myDict[imei] = cur_value+1

def processIMEIs(imeiList):
   uniqueCnt = 0
   totalCnt = 0
   for imei in imeiList:
      if imei:
         print "[main] Processing ",imei
         if findIMEI(imei):
            updateIMEI(imei)
         else:
            storeIMEI(imei)
            uniqueCnt += 1
         totalCnt += 1
   # print running total
   print "Total in this list  = ", totalCnt
   print "Unique in this list = ", uniqueCnt

   results['totalIMEI'] = results['totalIMEI'] + totalCnt 
   results['uniqueIMEI'] = results['uniqueIMEI'] + uniqueCnt 

myDict = {}

results = { 'totalIMEI' : 0, 'uniqueIMEI' : 0 }

imeiList =  ["aaaaaaaaaaaaaaaaaaa", "bbbbbbbbbbbbbbbbbbb","aaaaaaaaaaaaaaaaaaa"]
imeiList2 = ["aaaaaaaaaaaaaaaaaaa", "bbbbbbbbbbbbbbbbbbb","aaaaaaaaaaaaaaaaaaa"]
imeiList3 = ["aaaaaaaaaaaaaaaaaaaz", "bbbbbbbbbbbbbbbbbbbz","aaaaaaaaaaaaaaaaaaa"]

processIMEIs(imeiList)
print myDict
print results
processIMEIs(imeiList2)
print myDict
print results
processIMEIs(imeiList3)
print myDict
print results
