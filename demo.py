import CPS

from CPS import *

cps=CPSClient()
result=[]
IP='192.168.56.101'
# IP2='192.168.1.10'
port=10003
print(cps.HRIF_Connect(0,IP,port))
# print(cps.HRIF_Connect(1,IP2,port))
#print(cps.HRIF_ReadCurFSM(0,0,result))
#print(result)
# print(cps.HRIF_ReadCurFSM(1,0,result))
# print(result)

nRet = cps.HRIF_GrpEnable(0,0)