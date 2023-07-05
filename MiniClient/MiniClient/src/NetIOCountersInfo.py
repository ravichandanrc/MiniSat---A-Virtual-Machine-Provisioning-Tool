class NetIOCountersInfo:
    def __init__(self, netIOCounterName="", bytesSent=0, bytesRecv=0, packetsSent=0, packetsRecv=0, errin=0, errout=0, dropin=0, dropout=0):
        self.netIOCounterName = netIOCounterName 
        self.bytesSent = bytesSent 
        self.bytesRecv = bytesRecv
        self.packetsSent = packetsSent 
        self.packetsRecv = packetsRecv 
        self.errin = errin 
        self.errout = errout 
        self.dropin = dropin
        self.dropout = dropout