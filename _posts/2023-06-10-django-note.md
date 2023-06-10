---
layout: post
title: Django学习笔记
date: 2023-06-10
tags: Python
---

# 关闭Dango服务

## 方式1:在runserver启动终端下
```
执行Ctrl + c 可关闭Django服务。
```
## 方式2: 在其他终端下
``` 
执行 sudo Isof -i:8000 查询出Django的进程id。
执行 kill-9 对应Django进程id
```


