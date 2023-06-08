from CPS import CPSClient
import atexit
import time

cps = CPSClient()
IP='192.168.56.101'
port=10003
cps.HRIF_Connect(0,IP,port)
# @atexit.register
# def clean():
#     cps.HRIF_GrpStop(0, 0)

cps.HRIF_SetOverride(0, 0, 0.5)

points = [0,0,0,0,0,0]
RawACS1 = [0,10,30,0,90,0]
RawACS2 = [90,-50,30,0,40,80]
RawACS3 = [0,-50,30,0,40,-80]
tcp = 'TCP'
ucs = 'Base'
speed = 100
acc = 360
radius = 0
isJoint = 1
isSeek = 0
bit = 0
state = 0
cmdID = 0

while True:
    cps.HRIF_MoveJ(0, 0, points, RawACS1, tcp, ucs, speed, acc, radius, isJoint, isSeek, bit, state, cmdID)
    time.sleep(0.05)
    result = []
    msg = cps.waitMovementDone(0, 0, result)
    print(msg)

    cps.HRIF_MoveJ(0, 0, points, RawACS2, tcp, ucs, speed, acc, radius, isJoint, isSeek, bit, state, cmdID)
    time.sleep(1)
    msg = cps.waitMovementDone(0,0, result)
    print(msg)

    cps.HRIF_MoveJ(0, 0, points, RawACS1, tcp, ucs, speed, acc, radius, isJoint, isSeek, bit, state, cmdID)
    time.sleep(0.05)
    result = []
    msg = cps.waitMovementDone(0, 0, result)
    print(msg)

    cps.HRIF_MoveJ(0, 0, points, RawACS3, tcp, ucs, speed, acc, radius, isJoint, isSeek, bit, state, cmdID)
    time.sleep(1)
    msg = cps.waitMovementDone(0,0, result)
    print(msg)