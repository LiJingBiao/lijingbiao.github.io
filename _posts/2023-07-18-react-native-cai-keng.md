---
layout: post
title: ReactNative踩坑
date: 2023-07-18
tags: ios
---

## React Native默认运行真机，需要配置证书，如果要运行模拟器需要加模拟器
```
yarn ios --simulator 'iPhone 14Pro'
```

## [**React Navigation**](https://reactnavigation.org/)安装

```
npm install @react-navigation/native
npm install react-native-screens react-native-safe-area-context
npx pod-install ios
npm install @react-navigation/native-stack
```

