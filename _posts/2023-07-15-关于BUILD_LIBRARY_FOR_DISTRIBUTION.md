---
layout: post
title: 关于BUILD_LIBRARY_FOR_DISTRIBUTION
date: 2023-07-15
tags: iOS
---

在 CocoaPods 的 podspec 文件中,s.build_library_for_distribution 设置表示这个 pod 是否需要在集成时作为动态库进行编译。

它是一个布尔值,默认为 false。

如果设置为 true,表示这个 pod 会在集成时单独编译成一个动态库,然后主项目再链接这个动态库。

设置为 true 的常见场景有:

- pod 包含了 C/C++ 代码,需要编译成动态库后再集成到项目中。

- pod 中包含 Swift 代码,但主项目是 Objective-C,为了解决兼容性,需要将 Swift 代码编译成动态库。

- pod 对编译设置有特殊需求,需要作为动态库单独编译。

- pod 的作者想要对代码进行隐藏或者加密,不直接暴露在主项目中。

设置为 false 的场景:

- pod 只包含资源文件、Storyboard等,不需要编译操作。

- pod 中只包含 Objective-C/Swift 源码,可以直接汇编到主项目中。

- pod 不需要独立编译,引用它的项目也没有特殊需要。

所以这个选项主要影响 pod 在集成时的编译方式。设置为 true 后,pod 会作为一个独立的动态库进行编译。


在 CocoaPods 的 podspec 文件中,modular_headers 用于指定 Pod 在编译成动态库时需要暴露出去的公共头文件。

当 s.build_library_for_distribution 设置为 true 时,Pod 会编译成一个动态库。这个时候 Pod 中的私有头文件是不会暴露出去的,只有指定在 modular_headers 中的公共头文件才会对外暴露。

modular_headers 的格式如下:

```ruby
s.modular_headers = 'MyPod/PublicHeader1.h', 'MyPod/PublicHeader2.h'
```

指定了 modular_headers 后,在导入这个 Pod 的动态库时,只需要导入模块头文件,就可以访问对应的公共接口,无需再导入具体的头文件:

```objc
@import MyPod;
```

不指定 modular_headers 的话,默认会有一个模块头文件包含所有公共头文件。

使用 modular_headers 的好处是:

- 避免头文件污染,只暴露需要的公共接口。
- 引用 Pod 更加简单,只需要导入模块头文件。
- 可以按功能把公共头文件分组到不同模块头文件中。

所以 modular_headers 主要用于定义 Pod 编译成动态库后需要对外暴露的公共头文件,让 Pod 的接口更加清晰简洁。
