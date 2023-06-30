---
layout: post
title: flutter问题记录
date: 2023-06-29
tags: flutter
---

## 关于FFmpeg裁剪视频的问题

- 裁剪视频分辨率过高导致内存占用过高崩溃
- 视频格式导致跟苹果相册不兼容，导入不让保存到相册
```
-vcodec libx265 -vtag hvc1
```
- 视频裁剪过慢问题
```
-vcodec copy
```
- 视频前两秒黑屏
```
 -ss 0:00:00.000000 -to 0:00:30.000000 -accurate_seek -i 'IMG_0120.MP4' -vcodec copy  -preset ultrafast -y "1688027553401.mov"
```
- 视频上传太慢
视频压缩上传

## flutter跳转一个新的flutter(新的控制器)页面，flutterBoost导致pop上个页面无法接收到返回值

## 粘贴键不在输入框上方
## 调取原生方法map数据解析崩溃
## 安卓兼容性，无法获取图片宽高



