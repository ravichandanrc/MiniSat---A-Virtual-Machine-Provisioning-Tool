class DeviceInfo:
    def __init__(self, hostname, ipAddress, cores, logicalProcessors, bootTime, cpuTimesInfoList=[], cpuUsagePercList=[], virtualMemoryInfo=None, swapMemoryInfo=None, noOfPartitions=0, diskPartitionsInfoList=[], diskIOCountersInfo=None, netAddressInfo=None, netStatsInfoList=[], usersInfoList=[], netIOCountersInfoList=[], processInfoList=[]):
        self.hostname = hostname
        self.ipAddress  =  ipAddress
        self.cores = cores
        self.logicalProcessors = logicalProcessors
        self.bootTime = bootTime
        self.cpuTimesInfoList = cpuTimesInfoList
        self.cpuUsagePercList  = cpuUsagePercList
        self.virtualMemoryInfo = virtualMemoryInfo
        self.swapMemoryInfo = swapMemoryInfo
        self.noOfPartitions = noOfPartitions
        self.diskPartitionsInfoList = diskPartitionsInfoList
        self.diskIOCountersInfo = diskIOCountersInfo
        self.netAddressInfo = netAddressInfo
        self.netStatsInfoList  =  netStatsInfoList
        self.usersInfoList = usersInfoList
        self.netIOCountersInfoList = netIOCountersInfoList
        self.processInfoList = processInfoList


