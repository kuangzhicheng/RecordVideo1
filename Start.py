#-*-coding:utf-8-*-
from Video import Video
from os import path,mkdir

if __name__ == "__main__":
    while True:
        time = input("请输入录制时间:")
        OutPath = input("请输入存放径:")
        if time.isdigit():
            if not path.exists(OutPath):
                mkdir(OutPath)
            if int(time) < 10:
                time = 10
            video = Video(time,OutPath)
            try:
                video.Start()
            except Exception as e:
                print(e)
            break
        else:
            print("输入的信息有误，请重新输入")
            continue
    input("输入回车按键退出")
    print("增加打印Log")