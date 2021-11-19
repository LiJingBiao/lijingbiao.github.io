---
layout: post
title: flutter支持MacOS配置
date: 2021-11-19
tags: flutter
---
# 1、切换flutter channel
```
flutter channel dev
flutter upgrade

```

# 2、启用desktop开发支持
```
flutter config --enable-windows-desktop
flutter config --enable-macos-desktop
flutter config --enable-linux-desktop

```

# 3、检查环境
```
flutter doctor
```

# 4、创建flutter App

```
flutter create myapp
cd myapp

```

# 5、运行App

```
flutter run -d windows
flutter run -d macos
flutter run -d linux
```

# 5、Build a release app
```
flutter build windows
flutter build macos
flutter build linux

```

# 6、对已存在的App支持Desktop

```
flutter create --platforms=windows,macos,linux

```

参考:https://docs.flutter.dev/desktop




