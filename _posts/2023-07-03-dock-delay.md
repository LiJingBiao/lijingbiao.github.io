---
layout: post
title: 加速Dock显示
date: 2023-07-03
tags: mac
---

## 去除动画，立即显示Dock
```shell
defaults write com.apple.dock autohide-time-modifier -int 0;killall Dock
```

## 修改dock动画显示时间
```shell
defaults write com.apple.dock autohide-time-modifier -float 0.15;killall Dock
```

## 恢复默认设置
```shell
defaults delete com.apple.dock autohide-time-modifier;killall Dock
```
------

## 设置停靠多久显示dock
```shell
defaults write com.apple.dock autohide-delay -float 0; killall Dock
```
## 还原默认行为
```shell
defaults delete com.apple.dock autohide-delay; killall Dock
```
