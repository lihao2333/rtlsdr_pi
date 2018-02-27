#!/usr/bin/pyhon 
from rtlsdr import RtlSdrTcpServer
server = RtlSdrTcpServer(hostname='0.0.0.0', port=12345)
server.run_forever()
