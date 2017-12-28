#-*-coding:utf-8-*-
import os
class Devices(object):
    def __init__(self):
        super(Devices,self).__init__()
        self.Device = self.SetDevice()
        self.Resolution = self.SetResolution()
    def SetDevice(self):
        info = os.popen("adb devices").read()
        devices = info.split()
        if devices.__len__()<  5 :
            return None
        return info.split()[4]
    def SetResolution(self):
        if self.Device != None:
            info = os.popen('adb shell wm size').read()
            size = info.split()
            if size.__len__()<3:
               return None
            return size[2]




