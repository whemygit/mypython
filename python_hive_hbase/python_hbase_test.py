#!/usr/bin/env python
# -- coding: utf-8 --
import sys


import os
import time

from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift.transport import THttpClient
from thrift.protocol import TBinaryProtocol

reload(sys)
sys.setdefaultencoding("utf-8")

# Add path for local "gen-py/hbase" for the pre-generated module
gen_py_path = os.path.abspath('gen-py')
sys.path.append(gen_py_path)
from hbase import THBaseService
from hbase.ttypes import *

print "Thrift2 Demo"
print "This demo assumes you have a table called \"example\" with a column family called \"family1\""

# host = "117.78.40.175"
# host = "localhost"
host = "117.78.60.108"
port = 9090
framed = False

socket = TSocket.TSocket(host, port)
if framed:
  transport = TTransport.TFramedTransport(socket)
else:
  transport = TTransport.TBufferedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = THBaseService.Client(protocol)

transport.open()

table = "example"

put = TPut(row="row1", columnValues=[TColumnValue(family="family1",qualifier="qualifier1",value="value1")])
print "Putting:", put
# client.put(table, put)
#
# get = TGet(row="row1")
# print "Getting:", get
# result = client.get(table, get)
#
# print "Result:", result

transport.close()