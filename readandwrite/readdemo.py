#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
# if __name__ == '__main__':
#     print "test"

def writeFile(fileName,line):
    file_object = open(fileName, 'a')
    file_object.write(line)
    file_object.close()

# def readFile(fileName):
#     file_object = open(fileName)
#     try:
#         lines = file_object.readlines()
#         # for i in range(0,len(lines)):
#         #     if i % 2 == 0:
#         #         print i
#         #         writeFile("d:/myfile1.txt",lines[i])
#         #     else:
#         #         writeFile("d:/myfile2.txt",lines[i])
#         #         print i
#         i = 0;
#         for line in lines:
#             if i % 2 == 0:
#                 print i
#                 writeFile("d:/myfile1.txt",line)
#             else:
#                 writeFile("d:/myfile2.txt", line)
#             i = i + 1
#     finally:
#         file_object.close()




def genFileDict(fileName,num):
    dict = {}
    for i in range(num):
        tmpName = fileName + str(i+1) + ".txt"
        dict[i+1] = tmpName
    for k in dict:
        print k, dict[k]
    return dict

# 30 / 3 = 10
# import math
# def readFile(fileName,num):
#     file_object = open(fileName)
#     lines = file_object.readlines()
#     # mid =math.ceil(float(len(lines))/num)
#     mid=len(lines)/num
#     i = 1
#     j=1
#     # linenum = mid
#     for line in lines:
#         if j <= mid:
#
#             # print j
#             # print linenum
#             writeFile("d:/output"+str(i),line)
#             j+=1
#         else:
#             mid += mid
#             print mid
#             i+=1
#             writeFile("d:/output" + str(i), line)

import math
def readFile(fileName, num):
    file_object = open(fileName)
    lines = file_object.readlines()
    mid=math.ceil(float(len(lines))/num)
    # mid = len(lines) / num
    i = 1
    j=0
    chunk=mid
    for line in lines:
        if j >=chunk:
            chunk+=mid
            i+=1
        writeFile("d:/output" + str(i), line)
        j+=1


# readFile("D:/myfile/spider_output/test.txt")
readFile("d:/input.txt",3)
