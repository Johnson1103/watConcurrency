# base64是一种将不可见字符转换为可见字符的编码方式
import base64
# opencv是跨平台计算机视觉库，实现了图像处理和计算机视觉方面的很多通用算法
import os

import cv2
import requests
from aip import AipOcr
import numpy as np


# 百度AI的文字识别库

notListImage1 = []
def tailor_video(fileName):
    # 根目录
    v_path = 'e:/temp/' + fileName + '/'
    f_mp4 = os.listdir(v_path)
    sourceFileName = ''
    for x in f_mp4:
        if x.find('mp4') != -1:
            sourceFileName = x.split('.')[0]
    if sourceFileName != '':
        # 要提取视频的文件名，隐藏后缀
        # 在这里把后缀接上
        video_path = os.path.join("E:/temp/" + fileName + "/", sourceFileName + '.mp4')
        times = 0
        # 提取视频的频率，每10帧提取一个
        frameFrequency = 20
        # 输出图片到当前目录video文件夹下
        outPutDirName = 'E:/temp/' + fileName + '/image/'
        if not os.path.exists(outPutDirName):
            # 如果文件目录不存在则创建目录
            os.makedirs(outPutDirName)
            # notListImage1.append(fileName)
            camera = cv2.VideoCapture(video_path)
            while True:
                times += 1
                res, image = camera.read()
                if not res:
                    print('not res , not image')
                    break
                if times % frameFrequency == 0:
                    # cv2.imwrite(outPutDirName + str(times) + '.jpg', image)  # 文件目录下将输出的图片名字命名为10.jpg这种形式
                    # cv2.imencode(保存格式, 保存图片)[1].tofile(保存路径)
                    cv2.imencode('.jpg', image)[1].tofile(outPutDirName + str(times) + '.jpg')

                    print(outPutDirName + str(times) + '.jpg')
            print('图片提取结束')
    else:
        print('没有视频:' + fileName)


# 定义一个函数，用来判断是否是中文，是中文的话就返回True代表要提取中文字幕
def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


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


def main():
    print('1')
    # tailor_video()
    listdir = os.listdir('e:/temp/')

    for name in listdir:
        if name != 'video.csv':
            tailor_video(name)

    print('结果')
    print(len(notListImage1))


# 裁剪并进行灰度处理

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


if __name__ == '__main__':
    # main()
    # tailor_father()
    print(1)

