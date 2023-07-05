class NetStatsInfo:
    def __init__(self, netStatsName="", isup=False, duplex="", speed=0, mtu=0):
        self.netStatsName = netStatsName
        self.isup = isup
        self.duplex = duplex
        self.speed = speed
        self.mtu = mtu