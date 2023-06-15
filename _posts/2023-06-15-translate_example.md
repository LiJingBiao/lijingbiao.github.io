---
layout: post
title: 使用微软翻译翻译权限提示
date: 2023-06-15
tags: python
---

# 使用微软翻译翻译权限提示
```
import os

from translate import Translator
# translator=Translator(from_lang="cn",to_lang="english")
# translation = translator.translate("你好，世界！")
# print(translation)
import re
import json
from multiprocessing import Process
from threading import Thread

"""
English：en
Croatian：hr
English (Australia)：en-AU
French：fr
German：de
Indonesian：id
Italian：it
Japanese：ja
Russian：ru
Spanish：es
Turkish：tr
Ukrainian：uk
Vietnamese：vi

"""

all_lang_str = """
English：en
Croatian：hr
English (Australia)：en-AU
French：fr
German：de
Indonesian：id
Italian：it
Japanese：ja
Russian：ru
Spanish：es
Turkish：tr
Ukrainian：uk
Vietnamese：vi
"""

needTrans = {
    "NSCameraUsageDescription": "App需要您的同意,才能访问相机,用于上传头像和评论",
    "NSLocationUsageDescription": "App需要您的同意,才能访问定位,用于发送位置信息",
    "NSPhotoLibraryAddUsageDescription": "App需要您的同意,才能访问相片,用于上传头像和评论",
    "NSPhotoLibraryUsageDescription": "App需要您的同意,才能访问相册,用于上传头像和评论",
    "NSMicrophoneUsageDescription": "App需要您的同意,才能访问麦克风，用于发语音消息",
    "NSLocationWhenInUseUsageDescription": "App需要您的同意,才能访问定位,用于发送位置信息",
    "NSContactsUsageDescription": "App需要您的同意,才能访问通讯录，用于推荐好友服务",
}


def translate(originWord, to_lang):
    translator = Translator(from_lang="zh", to_lang=to_lang)
    return translator.translate(originWord)


result = {}


def transWithLang(lang):
    NSCameraUsageDescription = needTrans["NSCameraUsageDescription"]
    NSLocationUsageDescription = needTrans["NSLocationUsageDescription"]
    NSLocationWhenInUseUsageDescription = needTrans["NSLocationWhenInUseUsageDescription"]
    NSMicrophoneUsageDescription = needTrans["NSMicrophoneUsageDescription"]
    NSPhotoLibraryAddUsageDescription = needTrans["NSPhotoLibraryAddUsageDescription"]
    NSPhotoLibraryUsageDescription = needTrans["NSPhotoLibraryUsageDescription"]
    NSContactsUsageDescription = needTrans["NSContactsUsageDescription"]
    map = {}
    map["NSCameraUsageDescription"] = translate(NSCameraUsageDescription, lang)
    map["NSLocationUsageDescription"] = translate(NSLocationUsageDescription, lang)
    map["NSLocationWhenInUseUsageDescription"] = translate(NSLocationWhenInUseUsageDescription, lang)
    map["NSMicrophoneUsageDescription"] = translate(NSMicrophoneUsageDescription, lang)
    map["NSPhotoLibraryAddUsageDescription"] = translate(NSPhotoLibraryAddUsageDescription, lang)
    map["NSPhotoLibraryUsageDescription"] = translate(NSPhotoLibraryUsageDescription, lang)
    map["NSContactsUsageDescription"] = translate(NSContactsUsageDescription, lang)
    global result
    result[lang] = map
    # print(result)


all_lang = re.findall(r'(?<=：)[\w-]+', all_lang_str)

print(all_lang)
processes = []
for lang in all_lang:
    print(f"当前翻译:{lang}")
    p = Thread(target=transWithLang, args=(lang,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

print(f'result:{result}')
result = json.dumps(result)
print(f"{result}")
f = open('out_put1.txt','w')
f.write(result)
f.close()
exit(0)


f = open('out_put1.txt','r')
result = json.loads(f.read())

f.close()
for lang in all_lang:
    dir = lang + ".lproj"
    if not os.path.exists(dir):
        os.makedirs(dir)
    filePath = os.path.join(dir, 'InfoPlist.strings')
    print(filePath)
    langmap = result[lang]
    NSCameraUsageDescription = langmap["NSCameraUsageDescription"]
    NSCameraUsageDescription = f'NSCameraUsageDescription = "{NSCameraUsageDescription}";'

    NSLocationUsageDescription = langmap["NSLocationUsageDescription"]
    NSLocationUsageDescription = f'NSLocationUsageDescription = "{NSLocationUsageDescription}";'

    NSLocationWhenInUseUsageDescription = langmap["NSLocationWhenInUseUsageDescription"]
    NSLocationWhenInUseUsageDescription = f'NSLocationWhenInUseUsageDescription = "{NSLocationWhenInUseUsageDescription}";'

    NSMicrophoneUsageDescription = langmap["NSMicrophoneUsageDescription"]
    NSMicrophoneUsageDescription = f'NSMicrophoneUsageDescription = "{NSMicrophoneUsageDescription}";'

    NSPhotoLibraryAddUsageDescription = langmap["NSPhotoLibraryAddUsageDescription"]
    NSPhotoLibraryAddUsageDescription = f'NSPhotoLibraryAddUsageDescription = "{NSPhotoLibraryAddUsageDescription}";'

    NSPhotoLibraryUsageDescription = langmap["NSPhotoLibraryUsageDescription"]
    NSPhotoLibraryUsageDescription = f'NSPhotoLibraryUsageDescription = "{NSPhotoLibraryUsageDescription}";'

    NSContactsUsageDescription = langmap["NSContactsUsageDescription"]
    NSContactsUsageDescription = f'NSContactsUsageDescription = "{NSContactsUsageDescription}";'

    content = '\n\n\n' + NSCameraUsageDescription +'\n' + NSLocationUsageDescription +'\n' + NSLocationWhenInUseUsageDescription +'\n' + NSMicrophoneUsageDescription +'\n' + NSPhotoLibraryAddUsageDescription +'\n' + NSPhotoLibraryUsageDescription +'\n' + NSContactsUsageDescription
    with open(filePath, 'w+') as f:
        f.write(content)



```

# 有道翻译

```

# import requests
# data1 = {
#     'doctype': 'json',
#     'type': 'auto',
#     'i': '你好，世界！'
# }
# url = "http://fanyi.youdao.com/translate"
# response = requests.post(url, data=data1)
# result = response.json()
# print(result["translateResult"][0][0]["tgt"])


# -*- coding: utf-8 -*-
# Author:   玛卡巴卡
# Date:     2021/4/27 10:29
import requests
import hashlib
import time
import random


class YDDict(object):
    """有道翻译"""

    @staticmethod
    def get_data(keyword):
        """获取到其余的加密参数"""
        md = hashlib.md5()
        t = str(int(time.time() * 1000))
        i = t + str(random.randrange(10))
        md.update('fanyideskweb{}{}Tbh5E8=q6U3EXe+&L[4c@'.format(keyword, i).encode('utf8'))
        sign = md.hexdigest()
        return t, i, sign

    def translate(self, keyword='你好', data_from='AUTO', data_to='AUTO'):
        """
        对keyword进行翻译
        params: params_from 文本语言
        params: params_to 翻译成的语言类型
        """
        url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
            'Referer': 'https://fanyi.youdao.com/?keyfrom=fanyi-new.logo',
            'Host': 'fanyi.youdao.com',
            'Origin': 'https://fanyi.youdao.com',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
        }
        t, i, sign = self.get_data(keyword)
        data = {
            "i": keyword,
            "from": data_from,
            "to": data_to,
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": i,
            "sign": sign,
            "lts": t,
            # 这里bv是对UA加密得到的，所以也写成了定值
            "bv": "62c1eba97402d4ff4eb261254e974c27",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        response = requests.post(url, headers=headers, data=data)
        # json中包含结果，自己解析一下OK
        print(response.json())


if __name__ == '__main__':
    t = YDDict()
    t.translate(keyword='我是中国人', data_from= 'zh', data_to='JA')
```

# 谷歌翻译

```
from googletrans import Translator
translator = Translator()
result = translator.translate("你好，世界！", dest="en")
print(result.text)
```
