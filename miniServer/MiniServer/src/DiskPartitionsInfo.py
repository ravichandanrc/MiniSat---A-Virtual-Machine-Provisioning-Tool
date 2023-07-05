class DiskPartitionsInfo:
    def __init__(self, device="", mountpoint="", fstype="", opts="", total=0, used=0, free=0, percent=0):
        self.device = device
        self.mountpoint = mountpoint
        self.fstype = fstype
        self.opts = opts
        self.total = total
        self.used = used
        self.free = free
        self.percent = percent