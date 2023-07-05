import socket, pickle
import psutil
import datetime
import requests 
import os
import win32com.client
import re
import zipfile

from DeviceInfo import DeviceInfo
from CPUTimesInfo import CPUTimesInfo
from VirtualMemoryInfo import VirtualMemoryInfo
from SwapMemoryInfo import SwapMemoryInfo
from DiskIOCountersInfo import DiskIOCountersInfo
from DiskPartitionsInfo import DiskPartitionsInfo
from MemoryFullInfo import MemoryFullInfo
from MemoryInfo import MemoryInfo
from NetAddressInfo import NetAddressInfo
from NetStatsInfo import NetStatsInfo
from NetIOCountersInfo import NetIOCountersInfo
from ProcessCPUTimesInfo import ProcessCPUTimesInfo
from ProcessInfo import ProcessInfo
from UsersInfo import UsersInfo
from VirtualMemoryInfo import VirtualMemoryInfo



HOST = '127.0.0.1'  
PORT = 9999        






def getDeviceHealthInfo():
    
    
    hostname = socket.gethostname()    
    ipAddress = socket.gethostbyname(hostname)
    
    cores = psutil.cpu_count(logical=False) 
    print("No of Cores", cores)
    
    logicalProcessors = psutil.cpu_count() 
    
    
    bootTime = datetime.datetime.fromtimestamp(psutil.boot_time())
    

    '''
        user: time spent by normal processes executing in user mode
        system: time spent by processes executing in kernel mode
        idle: time spent doing nothing
        interrupt (Windows): time spent for servicing hardware interrupts
    '''
    
    cpuTimes = psutil.cpu_times(True)
    cpuTimesInfoList = []
    for cput in cpuTimes:
        print("cput", cput)
        cpuTimesInfo = CPUTimesInfo()
        cpuTimesInfo.user = cput.user
        cpuTimesInfo.system = cput.system
        cpuTimesInfo.idle = cput.idle
        cpuTimesInfo.interrupt = cput.interrupt
        cpuTimesInfoList.append(cpuTimesInfo)
    
    cpuUsagePerc = psutil.cpu_percent(interval=1, percpu=True)
    cpuUsagePercList=[]
    for cusa in cpuUsagePerc:
        cpuUsagePercList.append(cusa)  
    
    
    print("hostname", hostname)
    print("ipAddress", ipAddress)
    
    virtualMemoryInfo = VirtualMemoryInfo();
    vmem = psutil.virtual_memory()
    virtualMemoryInfo.percent = vmem.percent
    virtualMemoryInfo.total = vmem.total
    virtualMemoryInfo.used = vmem.used
    virtualMemoryInfo.free = vmem.free

    smem = psutil.swap_memory()
    swapMemoryInfo = SwapMemoryInfo()
    swapMemoryInfo.percent = smem.percent
    swapMemoryInfo.total = smem.total
    swapMemoryInfo.used = smem.used
    swapMemoryInfo.free = smem.free
    
    
    

    
    '''
    obj_Disk = psutil.disk_usage('/')

    print (obj_Disk.total / (1024.0 ** 3))
    print (obj_Disk.used / (1024.0 ** 3))
    print (obj_Disk.free / (1024.0 ** 3))
    print (obj_Disk.percent)

    disk_partitions = psutil.disk_partitions(all=False)
    print("No of Partitions ", len(disk_partitions))
    noOfPartitions = len(disk_partitions)
    diskPartitionsInfoList = []
    for partition in disk_partitions:
            diskPartitionsInfo = DiskPartitionsInfo()
            usage = psutil.disk_usage(partition.mountpoint)
            diskPartitionsInfo.device = partition.device
            diskPartitionsInfo.mountpoint= partition.mountpoint
            diskPartitionsInfo.fstype= partition.fstype
            diskPartitionsInfo.opts= partition.opts
            diskPartitionsInfo.total= usage.total
            diskPartitionsInfo.used= usage.used
            diskPartitionsInfo.free= usage.free
            diskPartitionsInfo.percent = usage.percent
            diskPartitionsInfoList.append(diskPartitionsInfo)
    
    
    
    diskIOCounters = psutil.disk_io_counters(perdisk=False)
    print("diskIOCounters ", diskIOCounters)
    diskIOCountersInfo = DiskIOCountersInfo()
    diskIOCountersInfo.readCount = diskIOCounters.read_count
    diskIOCountersInfo.writeCount = diskIOCounters.write_count
    diskIOCountersInfo.readBytes = diskIOCounters.read_bytes
    diskIOCountersInfo.writeBytes = diskIOCounters.write_bytes
    diskIOCountersInfo.readTime = diskIOCounters.read_time
    diskIOCountersInfo.writeTime = diskIOCounters.write_time
    
    
    netaddrs = psutil.net_if_addrs()
    print("netaddrs ", netaddrs)
    netAddressInfo = NetAddressInfo()
    for naddrKey, naddrValue in netaddrs.items():
        print("naddrKey ", naddrKey)
        netAddressInfo.netName = naddrKey
        nicAddrList = []
        for nicaddr in naddrValue:
            nicAddrList.append(nicaddr.address)
        netAddressInfo.nicAddrList= nicAddrList

    netstats = psutil.net_if_stats();
    print("netstats ", netstats)
    netStatsInfoList = []
    for key, value in netstats.items():
        netStatsInfo = NetStatsInfo()
        netStatsInfo.netStatsName = key
        netStatsInfo.isup = value.isup
        netStatsInfo.duplex = value.duplex
        netStatsInfo.speed = value.speed
        netStatsInfo.mtu = value.mtu
        netStatsInfoList.append(netStatsInfo)
        
    users = psutil.users()
    print("users ", users)
    usersInfoList = []
    for usr in users:
        usersInfo = UsersInfo()
        print("usr.name ", usr.name)
        print("usr.terminal ", usr.terminal)
        print("usr.started ", usr.started)
        usersInfoList.append(usersInfo)
    
    ncounters = psutil.net_io_counters(pernic=True)
    print("ncounters", ncounters)
    netIOCountersInfoList = []
    for counterKey, counterValue in ncounters.items():
        netIOCountersInfo = NetIOCountersInfo()
        netIOCountersInfo.netIOCounterName = counterKey
        netIOCountersInfo.bytes_sent = counterValue.bytes_sent
        netIOCountersInfo.bytes_recv = counterValue.bytes_recv
        netIOCountersInfo.packets_sent = counterValue.packets_sent
        netIOCountersInfo.packets_recv = counterValue.packets_recv
        netIOCountersInfo.errin = counterValue.errin
        netIOCountersInfo.errout = counterValue.errout
        netIOCountersInfo.dropin = counterValue.dropin
        netIOCountersInfo.dropout = counterValue.dropout
        netIOCountersInfoList.append(netIOCountersInfoList)
    
    processInfoList = []
    cnt = 0
    for proc in psutil.process_iter():
        cnt += 1
        if cnt > 200:
            break
        try:
            pinfo = proc.as_dict(attrs=['pid', "ppid", "status", 'name', 'username', "create_time", "cpu_percent", "cpu_times", "cwd", "memory_full_info", "memory_info", "memory_percent", "num_threads"])
        except psutil.NoSuchProcess:
            pass
        else:
            print("pinfo", pinfo)
            processInfo = ProcessInfo()
            processInfo.pid  = pinfo["pid"]
            processInfo.ppid  = pinfo["ppid"]
            processInfo.status  = pinfo["status"]
            processInfo.name  = pinfo["name"]
            processInfo.username  = pinfo["username"]
            processInfo.createTime  = pinfo["create_time"]
            processInfo.cpuPercent  = pinfo["cpu_percent"]
            processInfo.cwd  = pinfo["cwd"]
            processInfo.memoryPercent  = pinfo["memory_percent"]
            processInfo.numThreads  = pinfo["num_threads"]
            
            memoryFullInfo = MemoryFullInfo()
            if pinfo["memory_full_info"] != None:
                memoryFullInfo.rss = pinfo["memory_full_info"].rss
                memoryFullInfo.vms = pinfo["memory_full_info"].vms
                memoryFullInfo.peakWset = pinfo["memory_full_info"].peak_wset
                memoryFullInfo.wset = pinfo["memory_full_info"].wset
                memoryFullInfo.peakPagedPool = pinfo["memory_full_info"].peak_paged_pool
                memoryFullInfo.pagedPool = pinfo["memory_full_info"].paged_pool
                memoryFullInfo.peakNonPagedPool = pinfo["memory_full_info"].peak_nonpaged_pool
                memoryFullInfo.pagedNonPool = pinfo["memory_full_info"].nonpaged_pool
                memoryFullInfo.pageFile = pinfo["memory_full_info"].pagefile
            
            processInfo.memoryFullInfo  = memoryFullInfo
            
            memoryInfo = MemoryInfo()
            if pinfo["memory_info"] != None:
                memoryInfo.rss = pinfo["memory_info"].rss
                memoryInfo.vms = pinfo["memory_info"].vms
                memoryInfo.peakWset = pinfo["memory_info"].peak_wset
                memoryInfo.wset = pinfo["memory_info"].wset
                memoryInfo.peakPagedPool = pinfo["memory_info"].peak_paged_pool
                memoryInfo.pagedPool = pinfo["memory_info"].paged_pool
                memoryInfo.peakNonPagedPool = pinfo["memory_info"].peak_nonpaged_pool
                memoryInfo.pagedNonPool = pinfo["memory_info"].nonpaged_pool
                memoryInfo.pageFile = pinfo["memory_info"].pagefile
            
            processCPUTimesInfo = ProcessCPUTimesInfo()
            processCPUTimesInfo.user  = pinfo["cpu_times"].user
            processCPUTimesInfo.system  = pinfo["cpu_times"].system
            processCPUTimesInfo.childrenUser  = pinfo["cpu_times"].children_user
            processCPUTimesInfo.childrenSystem  = pinfo["cpu_times"].children_system
            processInfoList.append(processInfo)
    
    '''
    #deviceInfo = DeviceInfo(hostname, ipAddress, cores, logicalProcessors, bootTime, cpuTimesInfoList, cpuUsagePercList, virtualMemoryInfo, swapMemoryInfo, noOfPartitions, diskIOCountersInfo, netStatsInfoList, usersInfoList, netIOCountersInfoList)
    deviceInfo = DeviceInfo(hostname, ipAddress, cores, logicalProcessors, bootTime, cpuTimesInfoList, cpuUsagePercList, virtualMemoryInfo, swapMemoryInfo)
    return deviceInfo
#getDeviceHealthInfo()


def getComputerProcessInfo():
    processInfoList = []
    cnt = 0
    for proc in psutil.process_iter():
        cnt += 1
        if cnt >200:
            break
        try:
            pinfo = proc.as_dict(attrs=['pid', "ppid", "status", 'name', 'username', "create_time", "cpu_percent", "cpu_times", "cwd", "memory_full_info", "memory_info", "memory_percent", "num_threads"])
            print(type(pinfo["pid"]))
            if not str(pinfo["pid"]).isdigit() :
                continue 
            processInfo = ProcessInfo()
            processInfo.pid  = pinfo["pid"]
            processInfo.ppid  = pinfo["ppid"]
            processInfo.status  = pinfo["status"]
            processInfo.name  = pinfo["name"]
            processInfo.username  = pinfo["username"]
            processInfo.createTime  = pinfo["create_time"]
            processInfo.cpuPercent  = pinfo["cpu_percent"]
            processInfo.cwd  = pinfo["cwd"]
            processInfo.memoryPercent  = pinfo["memory_percent"]
            processInfo.numThreads  = pinfo["num_threads"]
            
            
            processInfoList.append(processInfo)

        except:
            pass
        else:
            pass
    return processInfoList

def killProcess(pid):
    try:
        prs = psutil.Process(pid)
        prs.kill()
        return True
    except:
        return False


def downloadAndUnzipSoftware(sname):

    if sname == "NodeJS":
        download_url = "https://nodejs.org/dist/v10.15.3/node-v10.15.3-win-x64.zip"
        r = requests.get(download_url)
        path = "download" 
        try:  
            os.mkdir(path)
        except OSError:  
                print ("Creation of the directory %s failed" % path)
        else:  
            print ("Successfully created the directory %s " % path)
        with open("download/nodejs.zip",'wb') as f:
            f.write(r.content)
            print("Node.js Successfully Downloaded")
            zip_ref = zipfile.ZipFile("download/nodejs.zip", 'r')
            zip_ref.extractall("installed/nodejs")
            zip_ref.close()
            return True
    return False
#downloadAndInstallSoftware("NodeJS") 

def getNotInstalledUpdates():
    print(1)
    keeper = win32com.client.Dispatch('Microsoft.Update.Session')
    print(2)
    seeker = keeper.CreateUpdateSearcher()
    print(3)
    availableUpdates = seeker.Search("Type='Software'")
    print(4)
    updates_pattern = re.compile(r'KB+\d+')
    print(5)
    notinstalled = []
    for update in availableUpdates.updates:
        for category in update.Categories:
            if not update.IsInstalled :
                update_code = updates_pattern.findall(str(update))
                tmp = "Name: " + str(update) + " - " + "url: " + "https://support.microsoft.com/en-us/kb/{}".format("".join(update_code).strip("KB")) + " - " + "Category: " + category.Name
                notinstalled.append(tmp)
                if len(notinstalled) > 25:
                    break
            print(update.IsInstalled)
        print(111)
        if len(notinstalled) > 25:
            break
    print(notinstalled)
    return notinstalled

def getInstalledUpdates():
    keeper = win32com.client.Dispatch('Microsoft.Update.Session')

    seeker = keeper.CreateUpdateSearcher()
    
    availableUpdates = seeker.Search("Type='Software' AND IsHidden=0")
    
    updates_pattern = re.compile(r'KB+\d+')
    
    installed = []
    for update in availableUpdates.updates:
        for category in update.Categories:
            if update.IsInstalled :
                update_code = updates_pattern.findall(str(update))
                tmp = "Name: " + str(update) + " - " + "url: " + "https://support.microsoft.com/en-us/kb/{}".format("".join(update_code).strip("KB")) + " - " + "Category: " + category.Name
                installed.append(tmp)
                if len(installed) > 25:
                    break
        if len(installed) > 25:
            break
    return installed   

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("CLient Listening in Port No "+str(PORT))
s.bind((HOST, PORT))
s.listen()


while True:
    conn, addr = s.accept()
    data = conn.recv(1024).decode('ascii')
    print('Connected by', addr)
    print(data)
    if data == 'GetDeviceInfo':
        print(data)
        devInfo = getDeviceHealthInfo()
        conn.sendall(pickle.dumps(devInfo))
        print("FInished..................................................................................")
        conn.close()
    if data == 'ContentManagementNotInstalled':
        print(data)
        notinstalled = getNotInstalledUpdates()
        conn.sendall(pickle.dumps(notinstalled))
        print("FInished..................................................................................")
        conn.close()
    if data == 'ContentManagementInstalled':
        print(data)
        installed = getInstalledUpdates()
        conn.sendall(pickle.dumps(installed))
        print("FInished..................................................................................")
        conn.close()
    if data == 'TerminateClientProcessListing':
        print(data)
        processInfoList = getComputerProcessInfo()
        conn.sendall(pickle.dumps(processInfoList))
        print("FInished..................................................................................")
        conn.close()
    if data.startswith('TerminateClientProcessPID'):
        data = data.replace("TerminateClientProcessPID", "")
        print(data)
        result = killProcess(int(data))
        conn.sendall(pickle.dumps(result))
        print("FInished..................................................................................")
        conn.close()
    if data.startswith('DownloadNodeJS'):
        print(data)
        result = downloadAndUnzipSoftware("NodeJS")
        conn.sendall(pickle.dumps(result))
        print("FInished..................................................................................")
        conn.close()
            #conn.sendall(data)