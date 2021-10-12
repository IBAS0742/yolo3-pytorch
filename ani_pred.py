import time

import cv2
import numpy as np
from PIL import Image

from yolo import YOLO
import pyautogui

yolo = YOLO()
#----------------------------------------------------------------------------------------------------------#
#   mode用于指定测试的模式：
#   'predict'表示单张图片预测，如果想对预测过程进行修改，如保存图片，截取对象等，可以先看下方详细的注释
#   'video'表示视频检测，可调用摄像头或者视频进行检测，详情查看下方注释。
#   'fps'表示测试fps，使用的图片是img里面的street.jpg，详情查看下方注释。
#   'dir_predict'表示遍历文件夹进行检测并保存。默认遍历img文件夹，保存img_out文件夹，详情查看下方注释。
#----------------------------------------------------------------------------------------------------------#
mode = "predict"
#-------------------------------------------------------------------------#
#   video_path用于指定视频的路径，当video_path=0时表示检测摄像头
#   video_save_path表示视频保存的路径，当video_save_path=""时表示不保存
#   video_fps用于保存的视频的fps
#   video_path、video_save_path和video_fps仅在mode='video'时有效
#   保存视频时需要ctrl+c退出或者运行到最后一帧才会完成完整的保存步骤。
#-------------------------------------------------------------------------#
video_path      = 0
video_save_path = ""
video_fps       = 25.0
#-------------------------------------------------------------------------#
#   test_interval用于指定测量fps的时候，图片检测的次数
#   理论上test_interval越大，fps越准确。
#-------------------------------------------------------------------------#
test_interval   = 100

while True:
    img = pyautogui.screenshot(region=[86,253,775,507]) # x,y,w,h (这里我取的是播放视频的视频内容位置)
    r_image = yolo.detect_image(img)
    img = cv2.cvtColor(np.asarray(r_image),cv2.COLOR_RGB2BGR)
    cv2.imshow("",img)
    cv2.waitKey(1)
    # img.save('screenshot.png')
    # img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)
    # r_image = yolo.detect_image(image)
