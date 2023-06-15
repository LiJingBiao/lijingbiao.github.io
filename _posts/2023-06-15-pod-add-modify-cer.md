---
layout: post
title: Podfile文件添加修改证书文件配置
date: 2023-06-15
tags: iOS
---

```
project_path = './MyApp.xcodeproj'
project = Xcodeproj::Project.open(project_path)

#修改某个target在debug模式下的证书配置
#此处遍历找到debug
project.targets[0].build_configurations.each do |config|
  config.build_settings['CODE_SIGN_STYLE'] = 'Manual'
  config.build_settings['CODE_SIGN_IDENTITY[sdk=iphoneos*]'] = 'iPhone Developer'
  config.build_settings['DEVELOPMENT_TEAM[sdk=iphoneos*]'] = '3341DSFSDF'
  config.build_settings['PROVISIONING_PROFILE_SPECIFIER[sdk=iphoneos*]'] = 'develop_test'
  config.build_settings['PRODUCT_BUNDLE_IDENTIFIER'] = 'com.xxxxxxxx.test'
  config.build_settings['PROVISIONING_PROFILE_SPECIFIER'] = ''
end

project.save
```
