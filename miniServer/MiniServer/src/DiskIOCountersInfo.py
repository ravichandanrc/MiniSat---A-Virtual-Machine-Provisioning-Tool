class DiskIOCountersInfo:
    def __init__(self, readCount=0, writeCount=0, readBytes=0, writeBytes=0, readTime=0, writeTime=0):
        self.readCount = readCount
        self.writeCount = writeCount
        self.readBytes = readBytes
        self.writeBytes = writeBytes
        self.readTime = readTime
        self.writeTime = writeTime