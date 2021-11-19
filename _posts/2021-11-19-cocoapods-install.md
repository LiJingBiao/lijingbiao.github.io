---
layout: post
title: Cocoapods卸载与安装
date: 2021-11-19
tags: cocoapods
---

## 1、查看CocoaPods组件安装位置：
```
which pod
```
结果：
```
/usr/bin/pod
```
## 2、手动移除这个组件：
```
sudo rm -rf /usr/bin/pod
```
## 3、移除RubyGems中的CocoaPods程序包
### 3.1、查看gems中本地程序包
```
gem list
```
### 3.2、移除程序包
有了版本号，就可以根据当前版本号移除CocoaPods了：
```
sudo gem uninstall cocoapods -v 1.5.3
sudo gem uninstall cocoapods-core
sudo gem uninstall fourflusher
```
## 4、修改 source 路径
### 4.1、删除 gem 源：
```
gem sources --remove https://gems.ruby-china.org
```
### 4.2、修改 gem 源：
```
gem sources -a https://gems.ruby-china.com
```
## 5、安装Cocoapods
### 5.1、安装Cocoapods
```
sudo gem install cocoapods
```
### 5.2、安装指定版本
```
sudo gem install -n /usr/local/bin cocoapods -v 1.5.3
```

