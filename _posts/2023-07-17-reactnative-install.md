---
layout: post
title: ReactNative环境安装
date: 2023-07-17
tags: iOS
---



# ReactNative环境安装

## 安装Node和watchman

```shell
brew install node@16
brew install watchman
```

`node@16` 中的`@16`表示安装 Node.js 16.x 系列的最新版本。

可选安装`yarn`,`yarn`Facebook 提供的替代 npm 的工具，可以加速 node 模块的下载

```
npm install -g yarn
```

## 创建新项目

```
npx react-native@latest init AwesomeProject
```

## 运行React Native项目

使用`npm`

```
npm run ios
```



```
yarn ios
```

## 运行报错点击查看

[跳转](https://reactnative.dev/docs/troubleshooting)

## 如果遇到`ios deploy`报错

```
sudo npm uninstall -g ios-deploy
brew install ios-deploy
```

