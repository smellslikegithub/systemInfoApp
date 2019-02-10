import platform as p
import datetime

class SystemInfo:
    #variables
    infoDict = {
        "memory": None,
        "freeMemory": None,
        "osDist": None,
        "system": None,
        "architecture":None,
        "machine":None,
        "node":None
    }
    timeStamp = 0

    def __init__(self):
        self.timeStamp = datetime.datetime.utcnow()
    
    def __getCpuInfo(self):
        with open("/proc/cpuinfo","r") as i:
            cpuInfo = i.readlines()
            for i in cpuInfo:
                i.strip().split(":")
                if("model name" in i):
                    self.infoDict["machine_model"] = i

    def __getMemoryInfo(self):
        with open("/proc/meminfo", "r") as i:
            memInfo = i.readlines()
            self.infoDict["memory"] = memInfo[0]
            self.infoDict["freeMemory"] = memInfo[1]
            
    def __operatingfSystemDistribution(self):
        self.infoDict["osDist"] = p.dist()
        
    def __systemInfo(self):
        self.infoDict["system"] = p.system()

    def __architecture(self):
        self.infoDict["architecture"] = p.architecture()[0]
    
    def __machine(self):
        self.infoDict["machine"] = p.machine()
    
    def __node(self):
        self.infoDict["node"] = p.node()

    def showAllInfo(self):
        self.__getCpuInfo()
        self.__getMemoryInfo()
        self.__operatingfSystemDistribution()
        self.__systemInfo()
        self.__architecture()
        self.__machine()
        self.__node()

        for key, value in self.infoDict.items():
            print (str(key) , str(value))
    