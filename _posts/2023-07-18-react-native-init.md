---
layout: post
title: ReactNative初始慢的问题
date: 2023-07-18
tags: iOS
---

创建RN工程有两种方式，一种是npx,一种是yarn的
```
# 第一种
npx react-native init RNProject
# 第二种
yarn create react-native-app RNProject
```

使用npx react-native init初始化React Native项目时需要下载很多依赖,会比较慢。有几种方法可以加速初始化过程:

1. 使用`yarn create react-native-app`代替`npx react-native init`。`yarn create`会cache模板,初始化速度会快很多。

2. 添加参数`--template`,直接使用本地的模板初始化项目,不需要下载模板:

```
npx react-native init MyApp --template [path to template]
```
3. 使用exponent/expo CLI,可以避免直接管理native代码,加速开发:
```
npm install -g expo-cli
expo init MyApp
```
4. 使用react-native-cli二进制包,可以避免下载cli: 
```
npm install -g react-native-cli
react-native init MyApp
```
5. 在初始化前配置npm registry为国内源,加速下载:
```
npm config set registry https://registry.npm.taobao.org
```
6. 使用缓存工具比如yarn cache或cnpm加速安装过程。

总之,使用本地模板、预编译的二进制包、国内源以及缓存可以显著提升react-native项目的初始化速度。

关于模版下载
React Native的初始化模板可以从几个地方获取:

1. React Native官方仓库: https://github.com/facebook/react-native/tree/master/template

直接把template文件夹下载到本地,然后初始化时通过--template参数指定。

2. Awesome React Native整理的模板列表: https://github.com/jondot/awesome-react-native#templates

这里整理了许多高质量的React Native项目模板,可以直接下载使用。

3. Expo提供的初始化模板: https://docs.expo.io/versions/latest/workflow/customizing/

Expo有自己的模板初始化项目,可以通过expo init开始。

4. 第三方模板比如Ignite、Pepper等: https://infinite.red/ignite

这些第三方模板通常会包含更多实用的功能模块,可以直接上手开发。

5. 自己创建并持续迭代的模板。

根据项目需求定制自己的初始化模板,并且随着时间不断完善。

综合考虑项目需求、团队偏好等选择一个合适的模板是一个不错的选择,可以帮助快速初始化项目。
