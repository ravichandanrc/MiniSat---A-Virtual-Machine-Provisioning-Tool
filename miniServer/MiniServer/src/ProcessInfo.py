class ProcessInfo:
    def __init__(self, pid="", ppid="", status="", name="", username="", createTime="", cpuPercent="", cwd="", processCPUTimesInfo=None, memoryFullInfo=None, memoryInfo=None, memoryPercent=0, numThreads=0):
        self.pid = pid
        self.ppid = ppid
        self.status = status
        self.name = name
        self.username = username
        self.createTime = createTime
        self.cpuPercent = cpuPercent
        self.processCPUTimesInfo = processCPUTimesInfo
        self.cwd = cwd
        self.memoryFullInfo = memoryFullInfo
        self.memoryInfo = memoryInfo
        self.memoryPercent = memoryPercent
        self.numThreads = numThreads