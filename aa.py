import requests
import json
import os


def getList(startInt):
    fid = 'fd7375b9-d304-4d50-852a-c4d0f6c827fc'

    url = 'http://localhost:8080/homeController/getRemainingFolderView.ajax'

    params = {'fid': fid, 'foldersOffset': startInt, 'fileOffset': 0}

    # headers = {'content-type': 'text/html;charset=utf-8'}
    headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Cookie': 'folder_id=fd7375b9-d304-4d50-852a-c4d0f6c827fc; notice_md5=mustLogin; JSESSIONID=D5099F5B563ABC2D2E019FA45F2C74E1'}

    response = requests.post(url, data=params, headers=headers, verify=False)

    tempStr = json.loads(response.text)
    arr = tempStr['folderList']

    return arr


def _removeDir(root):
    listDir = os.listdir(root)
    for fileName in listDir:
        if os.path.isfile(root + fileName):
            os.remove(root + fileName)
        else:
            _removeDir(root + fileName + '/')
            os.removedirs(root + fileName + '/')


if __name__ == "__main__":
    # startInt = 1004
    # dirList1 = []
    # while True:
    #     arrOK = getList(startInt)
    #     dirList1 += arrOK
    #     if startInt > 255:
    #         startInt -= 256
    #     else:
    #         break
    #
    # dirList = os.listdir('e:/temp')
    # dirList.remove('video.csv')
    # yscList = []
    # wscList = []
    #
    # for x in dirList1:
    #     yscList.append(x['folderName'])
    # print(len(yscList))
    # print('yscList')
    # print(yscList)
    # for x in dirList:
    #     if x == '绿玉树':
    #         print('##')
    #     if x in yscList:
    #         print(x + '已经上传')
    #     else:
    #         print(x + '未上传')
    #         wscList.append(x)
    #
    # print('###未上传的数量为' + str(len(wscList)))
    # print('分别是:')
    # for y in wscList:
    #     print(y)
    path = 'e:/temp/'
    listdir = os.listdir(path)
    listdir.remove('video.csv')
    for name in listdir:
        print('来了')
        try:
            if os.path.exists(path + name + '/image/'):
                _removeDir(path + name + '/image/')
        except Exception as e:
            print(e)

