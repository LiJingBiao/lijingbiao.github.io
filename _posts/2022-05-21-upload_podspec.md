---
layout: post
title: 上传PodSpec脚本
date: 2022-05-21
tags: shell
---


```
#!/bin/bash

git stash
git pull origin master --tags
git stash pop

VersionString=`grep -E 's.version.*=' XXXX.podspec`
VersionNumber=`tr -cd 0-9 <<<"$VersionString"`
NewVersionNumber=$(($VersionNumber + 1))
LineNumber=`grep -nE 's.version.*=' XXXX.podspec | cut -d : -f1`

git add .
git commit -am modification
git pull origin master --tags

sed -i "" "${LineNumber}s/${VersionNumber}/${NewVersionNumber}/g" XXXX.podspec

echo "current version is ${VersionNumber}, new version is ${NewVersionNumber}"

git commit -am ${NewVersionNumber}
git tag ${NewVersionNumber}
git push origin master --tags
pod trunk push ./XXXX.podspec --verbose --use-libraries --allow-warnings

```
