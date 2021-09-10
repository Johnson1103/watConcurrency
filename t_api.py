import os

import requests
import base64

ACCESS_TOKEN = '24.35c610847667e50d7a3c4ebb7c99e0d6.2592000.1628837486.282335-24545798'


# 定义一个函数，用来访问百度API，
def requestApi(img):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"

    params = {"image": img, 'language_type': 'CHN_ENG'}

    access_token = '24.b802cd212b0e702b018f999c594b6d9f.2592000.1589466832.282335-19430506'

    request_url = request_url + "?access_token=" + ACCESS_TOKEN

    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.post(request_url, data=params, headers=headers, timeout=10)

    results = response.json()

    return results


def getAccessToken():
    SECRET_KEY = 'SZOkeIveE8D5BCY1jGUD43W5ZHD6zKv3'
    API_KEY = 'tFoHLAg8a1DpECrFv1Geqfu5'

    request_url = 'https://aip.baidubce.com/oauth/2.0/token'
    params = {'client_secret': SECRET_KEY, 'client_id': API_KEY, 'grant_type': 'client_credentials'}
    response = requests.post(request_url, data=params)
    response.json()['access_token']


def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        # 将读取出来的图片转换为b64encode编码格式
        return base64.b64encode(fp.read())


# 定义函数字幕，用来对字幕进行操作

def text_create(name, msg):
    # desktop_path = "e:/txt/"  # 新创建的txt文件的存放路径
    full_path = name + '/字幕.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w')
    file.write(msg)
    file.close()


# step_size 步长
def subtitle(fname, listImg, listImgName):
    array = []  # 定义一个数组用来存放words
    for i in listImg:
        fname1 = fname % str(i)
        image = get_file_content(fname1)
        try:
            results = None
            connectNum = 0
            while connectNum < 3:
                try:
                    results = requestApi(image)['words_result']  # 调用requestApi函数，获取json字符串中的words_result
                    break
                except requests.exceptions.RequestException as e:
                    
                    print('失败，请求重试')
                    connectNum += 1

            if results is not None:
                print(results)
                if isinstance(results, list) and len(results) >= 0:
                    array.append(results[0]['words'])
        except Exception as e:
            print(e)

    text = ''
    result = list(set(array))  # 将array数组准换为一个无序不重复元素集达到去重的效果，再转为列表
    result.sort(key=array.index)  # 利用sort将数组中的元素即字幕重新排序，达到视频播放字幕的顺序
    for item in result:
        print(item)
        text += item + '\n'
    text_create(listImgName, text)


# 去重并且拼接
# def setItem(item):


def caijian():
    path = 'e:/temp/'
    pathImage = ''
    listDir = os.listdir(path)
    num = 0;
    for name in listDir:
        if name == 'video.csv':
            continue

        # 判断是否已经执行过
        hasZimu = os.listdir(path + name)
        flag = True
        for temp in hasZimu:
            if temp == '字幕.txt':
                flag = False
        if flag:
            pathObj = path + name + '/image/image1/%s.jpg'
            print('处理---' + name)
            listImgDir = os.listdir(path + name + '/image/image1/')
            listImg = []
            for imageTemp in listImgDir:
                if imageTemp.find('.jpg') != -1:
                    listImg.append(int(imageTemp.split('.')[0]))
            listImg.sort(reverse=False)
            listImg1 = []
            for imageTemp in listImg:
                if os.path.getsize(path + name + '/image/image1/' + str(imageTemp) + '.jpg') > 5000:
                    listImg1.append(imageTemp)
            subtitle(pathObj, listImg1, path + name)
            num += 1
            print('当前处理第' + str(num) + '个')
        else:
            num += 1
            print(str(num) + '-----' +name +'已经执行过了。跳过')
            continue
    print('执行完毕，共执行' + str(num))


if __name__ == '__main__':
    # getAccessToken()
    # subtitle('e:/temp/䴙（pì）䴘（tī）/image/image1/%s.jpg', [1580])
    caijian()

