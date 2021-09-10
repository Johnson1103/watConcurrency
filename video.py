import requests
import base64
import time
import os


def get_video_list(p_id, id):
    headers = {
        'referer': 'https://www.ixigua.com/'
    }
    # 每次获取30个视频，注意大与30可能存在采集不完全的情况
    url = f'https://www.ixigua.com/api/videov2/author/new_video_list?to_user_id= {id}&offset={p_id}&limit=30'
    res = requests.get(url=url, headers=headers)
    return res.json()


def get_video_url(video_id):
    url = f'https://www.ixigua.com/api/public/videov2/brief/details?group_id={video_id}'
    res = requests.get(url=url)
    data = res.json()['data']['videoResource']['normal']['video_list']['video_3']['main_url']
    return base64.b64decode(data)


def save_video(name, url, root):
    res = requests.get(url)
    data = res.content
    file_name = name.split('——')[0]
    if not os.path.exists(root + file_name):
        os.mkdir(root + file_name)
    with open(root + file_name + '/' + name + '.mp4', 'wb+') as f:
        f.write(data)
    print(f'{name}下载完成！')


def main():
    # 保存路径 相对路径绝对路径都行 注意结尾一定带/
    root = 'e:/temp/'
    # 采集的用户id
    user_id = '800093389722574'
    # 页数，从0页开始，每次采集30个
    p_id = 0
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(root + 'video.csv'):
        with open(root + 'video.csv', 'w+') as f:
            f.write('title,url\n')

    while True:
        video_list = get_video_list(p_id, user_id)
        for i in video_list['data']['videoList']:
            title = i['title']
            v_id = i['gid']
            url = get_video_url(v_id)
            save_video(title, url, root)
            with open(root + 'video.csv', 'a') as f:
                f.write(f'{title},https://www.ixigua.com/{v_id}\n')
        if len(video_list['data']['videoList']) < 30:
            print(len(video_list['data']['videoList']))
            break
        p_id += 30


if __name__ == '__main__':
    main()
