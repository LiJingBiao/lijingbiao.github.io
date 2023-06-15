import os
import re
import subprocess
currentDir = os.path.dirname(os.path.abspath(__file__))
postDir = os.path.join(currentDir, '_posts')
# print(currentDir)
# print(postDir)
allFiles = [os.path.join(postDir, file) for file in os.listdir(postDir) if
            os.path.isfile(os.path.join(postDir, file)) and (not file.startswith(r'.'))]
allFiles.sort(key=lambda x: os.path.getmtime(x), reverse=True)
lastPost = allFiles[0]
title = ''
with open(lastPost,mode='r') as f:
    content = f.read()
    # print(content)
    match = re.search(r'(?<=title:\s)\S+',content)
    if match.group():
        title = match.group()

commitMsg = f'更新【{title}】'

cmd = 'git pull && git add -A'
returned_value = subprocess.call(cmd, shell=True)
if returned_value != 0:
    print('\033[31;1m 【add失败】  \033[0m')
    exit(-1)
cmd = 'git commit -m ' + commitMsg
returned_value = subprocess.call(cmd, shell=True)
if returned_value != 0:
    print('\033[31;1m 【commit失败】  \033[0m')
    exit(-1)

cmd = 'git push'
returned_value = subprocess.call(cmd, shell=True)
if returned_value != 0:
    print('\033[31;1m 【push失败】  \033[0m')
    exit(-1)
print("\033[32;1m 提交成功 🎉  🎉  🎉   \033[0m")

# print(returned_value)
# cmd = 'git push'
# returned_value = subprocess.call(cmd, shell=True)
# print(returned_value)

# print(title)
    # print(match)
    # print(content)
# print(lastPost)
# print(allFile)
# lastPostFile = allFile[0]
# print(lastPostFile)

# for file in os.listdir(postDir):
#     print(file)
