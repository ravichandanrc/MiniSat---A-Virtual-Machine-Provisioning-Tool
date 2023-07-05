class ProcessCPUTimesInfo:
    def __init__(self, user=0, system=0, childrenUser=0, childrenSystem=0):
        self.user = user
        self.system = system
        self.childrenUser = childrenUser
        self.childrenSystem = childrenSystem