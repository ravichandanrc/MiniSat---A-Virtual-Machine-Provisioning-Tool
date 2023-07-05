class CPUTimesInfo:
    def __init__(self, user="", system="", idle="", interrupt=""):
        self.user = user
        self.system = system
        self.idle = idle
        self.interrupt = interrupt