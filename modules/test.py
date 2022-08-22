import pysnmp
from pysnmp.hlapi import *

oid = "1.3.6.1.4.1.48690.1.1.0"
address = '192.168.1.1'

iterator = getCmd(
    SnmpEngine(),
    CommunityData('public', mpModel=0),
    UdpTransportTarget((address, 161)),
    ContextData(),
    ObjectType(ObjectIdentity(oid)))


errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

if errorIndication:
    print(errorIndication)

elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))