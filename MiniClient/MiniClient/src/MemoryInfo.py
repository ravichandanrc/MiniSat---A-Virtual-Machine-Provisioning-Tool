class MemoryInfo:
    def __init__(self, rss=0, vms=0, peakWset=0, wset=0, peakPagedPool=0, pagedPool=0, peakNonPagedPool=0, pagedNonPool=0, pageFile=0):
        self.rss = rss
        self.vms = vms
        self.peakWset = peakWset
        self.wset = wset
        self.peakPagedPool = peakPagedPool
        self.pagedPool = pagedPool
        self.peakNonPagedPool = peakNonPagedPool
        self.pagedNonPool = pagedNonPool
        self.pageFile = pageFile