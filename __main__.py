# -*- coding: utf-8 -*-
# Copyright 2020 © Zerocat Frp & Xiao_Jin. All rights reserved.
# Author: Xiao_Jin

import requests
import os
from pyfiglet import Figlet


class ZerocatFrpClient:
    def __init__(self):
        self.query_url_of_key = 'https://www.zerofrp.com/key/'  # 旧API地址
        self.path_of_cache = 'zerocat-frp.key'
        self.user_key = None

        self.app()

    @staticmethod
    def welcome():
        os.system('title Zerocat Frp Client')
        f = Figlet(font='big')
        print(f.renderText('Zerocat Frp'))
        print('\t\t公网云 - 免费一键映射内网穿透\n\n\n')

    def if_cache(self):
        if os.path.exists(self.path_of_cache):  # 存在就快速登录
            with open(self.path_of_cache, 'r') as key_file:
                self.user_key = key_file.readline()
        else:  # 不存在就输入
            self.when_no_cache()

    def when_no_cache(self):
        eula_req = requests.get('https://lab.xiao-jin.xyz/zerocat-frp/eula')
        eula = eula_req.text
        print(eula)  # 仅在没有本地缓存时提示EULA，不烦人
        self.user_key = input('\n\n\n这好像是您第一次使用呢，请输入您的穿透KEY >>>')

    def verify_key(self):
        print('正在获取隧道信息。。。')
        query_request = requests.get(self.query_url_of_key, params={'key': self.user_key})
        query_ans = query_request.json()

        # 验证登录是否成功
        if query_request.headers['X-Status'] == 'ok':
            # 不存在key的本地缓存时创建一个
            if not os.path.exists(self.path_of_cache):
                with open(self.path_of_cache, 'w+') as key_file:
                    key_file.write(self.user_key)
                    print('您以后就可以一键启动了呢QwQ')

            print('登录成功，获取到配置文件')
            print(query_ans)
        else:
            print('额。好像出了什么问题呢。。')
            print('> HTTP状态码：' + str(query_request.status_code))
            print('> 错误报告：' + query_request.text)
    
    def app(self):
        self.welcome()
        self.if_cache()


if __name__ == '__main__':
    ZerocatFrpClient()
