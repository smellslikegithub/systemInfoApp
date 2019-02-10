import platform as p
import datetime

class SystemInfo:
    #variables
    infoDict = {
        "timestamp":"",
        "machine_model":"hello"
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
    
    def showAllInfo(self):
        self.__getCpuInfo()
        print(self.infoDict["machine_model"])