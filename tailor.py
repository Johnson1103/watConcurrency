
import base64
# opencv是跨平台计算机视觉库，实现了图像处理和计算机视觉方面的很多通用算法
import os

import cv2
import requests
from aip import AipOcr
import numpy as np


def tailor_father():
    listdir = os.listdir('e:/temp/')
    for dirName in listdir:
        if dirName != 'video.csv':
            path = 'e:/temp/' + dirName + '/'
            path1 = path + 'image/%s.jpg'

            if not os.path.exists(path + 'image/'):
                continue

            if not os.path.exists(path + 'image/image1/'):
                os.mkdir(path + 'image/image1/')
            else:
                continue

            path2 = path + 'image/image1/%s.jpg'
            imageDir = os.listdir(path + 'image')
            maxArr = []

            for imageDirName in imageDir:
                if imageDirName.find('.jpg') != -1:
                    maxArr.append(int(imageDirName.split('.')[0]))

            maxArr.sort(reverse=True)
            tailor(path1, path2, 20, maxArr[4] + 1, 20)


def tailor(path1, path2, begin, end, step_size):  #截取字幕
    for i in range(begin, end, step_size):
        fname1 = path1 % str(i)
        print(fname1)
        # img = cv2.imread(fname1)
        img = cv2.imdecode(np.fromfile(fname1, dtype=np.uint8), -1)
        print(img.shape)
        cropped = img[598:713, 100:1300]  # 裁剪坐标为[y0:y1, x0:x1]
        imgray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
        thresh = 200
        ret, binary = cv2.threshold(imgray, thresh, 255, cv2.THRESH_BINARY)  # 输入灰度图，输出二值图
        binary1 = cv2.bitwise_not(binary)  # 取反
        # cv2.imencode(path2 % str(i), binary1)
        cv2.imencode('.jpg', binary1)[1].tofile(path2 % str(i))