#-*-coding:utf-8-*-
from os import system
from Dervices import Devices

class Video(object):
    def __init__(self,RecordTime =30,OutPath="C:\\Screenrecord",InPutPath ="/sdcard/Demo.mp4",Bitrate = 6000000,):
        self.RecordTime = RecordTime
        self.Bitrate = Bitrate
        self.InPutPath =InPutPath
        self.OutPath = OutPath
    def Start(self):
        device = Devices()
        if device.Device == None or device.Resolution == None:
            raise Exception("没有检测到设备,是否开启调试模式")
        command = "adb shell screenrecord --bit-rate {0} --size {1} --time-limit {2} {3}".format(self.Bitrate,device.Resolution,self.RecordTime,self.InPutPath)
        print("开始录制ing")
        system(command)
        command = "adb pull {0} {1}".format(self.InPutPath,self.OutPath)
        system(command)
        system("start %s"%self.OutPath)


