# -*- coding: utf-8 -*-
# Copyright 2020 © Zerocat Frp & Xiao_Jin. All rights reserved.
# Author: Xiao_Jin & ♡·小幸福♡

import requests
import os
from pyfiglet import Figlet


def app():
    os.system('title Zerocat Frp Client')
    f = Figlet(font='big')
    print(f.renderText('Zerocat Frp'))
    print('\t\t公网云 - 免费一键映射内网穿透\n\n\n')
    eula = '''> 使用此服务，表示您已同意以下的规定
> 
> 1.请不要攻击节点。
> 2.请不要搭建黄色、赌博、钓鱼网站。
> 3.本工具仅针对无公网用户有效,有公网用户就把机会让给没有公网的人吧。
> 4.使用本穿透工具请先阅读文件夹里的使用说明。
> 5.使用本穿透工具造成的损失本平台不承担任何法律责任。
> 6.本网站服务为公益服，有权终止本网站的任何服务'''

    # TODO: 使用新的API
    query_url_of_key = 'https://www.zerofrp.com/key/'  # 旧API地址
    path_of_key = 'zerocat-frp.key'

    # 判断KEY的本地缓存是否存在
    if os.path.exists(path_of_key):  # 存在就快速登录
        with open(path_of_key, 'r') as key_file:
            user_key = key_file.readline()
    else:  # 不存在就输入
        print(eula)  # 仅在没有本地缓存时提示EULA，不烦人
        user_key = input('\n\n\n这好像是您第一次使用呢，请输入您的穿透KEY >>>')

    print('正在获取隧道信息。。。')
    query_request = requests.get(query_url_of_key, params={'key': user_key})
    query_ans = query_request.json()

    # 验证登录是否成功
    if query_ans['status'] == 'ok':
        # 不存在key的本地缓存时创建一个
        if not os.path.exists(path_of_key):
            with open(path_of_key, 'w+') as key_file:
                key_file.write(user_key)
                print('您以后就可以一键启动了呢QwQ')

        print('登录成功，获取到配置文件')
        print(query_ans)
    else:
        print('额。好像出了什么问题呢。。')
        print('> HTTP状态码：'+str(query_request.status_code))
        print('> 错误报告：'+query_request.text)
    # TODO: 使用INI文件启动frpc


if __name__ == '__main__':
    app()
