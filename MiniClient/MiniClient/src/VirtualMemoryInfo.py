class VirtualMemoryInfo:
    def __init__(self, percent=0, total=0, used=0, free=0):
        self.percent = percent
        self.total = total
        self.used = used
        self.free = free