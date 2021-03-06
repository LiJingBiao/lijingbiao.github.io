---
layout: post
title: Shell笔记
date: 2021-04-01
tags: Shell
---

## 1、Mac下shell别名，可以在`/etc/bashrc` 或者`~/.bash_profile`添加
```
alias grep='grep --color=auto'
```
## 2、变量赋值等号两边每空格
```
A="Hello world"
```
## 3、expr 运算符两边有空格
```
expr 2 + 3
```
## 4、条件判断[ 条件判断 ] [[ 条件判断 ]]两边有空格
## 5、条件判断中运算符两边有空格
```
[ ! $(id -u) -eq 0 ] && echo "ABC"
```
## 5、表达式
```
#表达式空格可有可无，两个表达式相等
$((1+3))
$[1+3]
```

## 6、类C风格((A=1))赋值,((A==B))判等

## 7、如果需要在文件中替换多个相同的字符串，需要添加global参数g，即:
```
sed -i ".bak" "s/1.*/aa\/bb/g" test.txt
或者
#https://blog.csdn.net/toopoo/article/details/104432196
sed -i ".bak" "s|1.*|aa/bb|g" test.txt
```

## 8、字符串操作
```
${#string} : $string 的长度
${string:position} : 从$position位置开始的子字符串
${string:position:length} : 从$position位置开始，长度为length的子字符串
${string#substring} : 从头开始，删除最短匹配$substring的字符串
${string##substring} : 从头开始，删除最长匹配$substring的字符串
${string%substring} : 从结尾开始，删除最短匹配$substring的字符串
${string%%substring} : 从结尾开始，删除最长匹配$substring的字符串
${string/str1/str2} : 使用str2替换第一个匹配的$str1
${string//str1/str2} : 使用str2替换所有匹配的$str1
${string/#str1/str2} : 如果$string的前缀和$str1匹配,用$str2替换$str1
${string/%str1/str2} : 如果$string的后缀和$str1匹配，用$str2替换$str1


${file-my.file.txt} ：假如$file 沒有设定，則使用my.file.txt 作传回值。(空值及非空值時不作处理) 
${file:-my.file.txt} ：假如$file 沒有設定或為空值，則使用my.file.txt 作傳回值。(非空值時不作处理)
${file+my.file.txt} ：假如$file 設為空值或非空值，均使用my.file.txt 作傳回值。(沒設定時不作处理)
${file:+my.file.txt} ：若$file 為非空值，則使用my.file.txt 作傳回值。(沒設定及空值時不作处理)
${file=my.file.txt} ：若$file 沒設定，則使用my.file.txt 作傳回值，同時將$file 賦值為my.file.txt 。(空值及非空值時不作处理)
${file:=my.file.txt} ：若$file 沒設定或為空值，則使用my.file.txt 作傳回值，同時將$file 賦值為my.file.txt 。(非空值時不作处理)
${file?my.file.txt} ：若$file 沒設定，則將my.file.txt 輸出至STDERR。(空值及非空值時不作处理)
${file:?my.file.txt} ：若$file 没设定或为空值，则将my.file.txt 输出至STDERR。(非空值時不作处理)

${#var} 可计算出变量值的长度：
```
## 9、从文本中读取字符串命令执行
```
awk '/^TN/{ cmd=$0; system(cmd) }' $SRCROOT/../README.md
```
## 10、获取当前目录
```
project_path=$(cd "`dirname "$0"`"; pwd)
#当前目录
cur_dir=$(pwd)
#上级目录
highter_dir=$(dirname "$(pwd)")
```
获取路径最后一个名字
```
project_path=$(cd "`dirname "$0"`"; pwd)
#当前目录
cur_dir=$(pwd)
#上级目录
highter_dir=$(dirname "$(pwd)")
```
## 11、懒加载代码
```
#!/bin/bash
iosBatchLazyCode(){
	
	if test $1 = "UIButton" ; then
   		str="[$1 buttonWithType:UIButtonTypeCustom];"
   	else
   		str="[[$1 alloc]init];"
	fi
  echo -e "
- ($1 *)$2{
    if (_$2 == nil) {
        _$2 = $str
    }
    return _$2;
}" 
}

#追加一行空格
echo -e '\n' >> propertys.txt

#读取文件存数组
i=0
while read line
do
	lineStr=$line
	noneSpaceStr=${lineStr// /}
    ARR[$i]=$noneSpaceStr
    let i+=1
done < propertys.txt

#格式化输出到out.txt
for str in ${ARR[*]}
do
	a=${str#*)}
	b=${a%"*"*}

	c=${str#*"*"}
	d=${c%*;}
	iosBatchLazyCode $b $d 
done >> out.txt 

```
## 12、创建文件
```
RESOURCES_TO_COPY=${PODS_ROOT}/resources-to-copy-${TARGETNAME}.txt
> "$RESOURCES_TO_COPY"
```
## 13、字符串正则匹配

```
str1=我是中国人
if [[ "$str1" == 我是* ]]; then
     echo 有前缀
else
     echo 没有前缀
fi
```

## 14、shell替换空格

- 方法1

```
"21241       2412  " | sed s/[[:space:]]//g
```

- 方法2

```
awk -F: 'BEGIN{};/cdtp_dns_router/{ gsub(/[[:blank:]]*/,"",$0);print $0 }' $SRCROOT/../README.MD
```

## 15、将查找的字符串转换为命令

```
`awk '/^TN/{print $0; system($0)}' ./README.MD`

#第二种方法
export LANG=en_US.UTF-8

$(pod repo update 6-toon_pod_spec)

awk 'BEGIN{ORS="~"};/^TN/{print $0}' ../README.md | cut -d~ -f1|awk '{sub(/[[:blank:]]*$/,"",$0); system($0)}'

```

## 16、awk清除空格

```
sub(/^[[:blank:]]*/,"",变量)  #是去掉变量左边的空白符
sub(/[[:blank:]]*$/,"",变量)  #是去掉变量右边的空白符
gsub(/[[:blank:]]*/,"",变量)  #是去掉变量中所有的空白符
```
示例：
```
echo ' 123 456 789  ' | awk '{
print "<" $0 ">";
sub(/^[[:blank:]]*/,"",$0);print "[" $0 "]";
sub(/[[:blank:]]*$/,"",$0);print "|" $0 "|";
gsub(/[[:blank:]]*/,"",$0);print "/" $0 "/";
```
gsub返值是替换次数，而不是替换结果。


## 17、shell下alias 添加参数

`alias` 默认是无法添加参数的，要想添加参数，只能定义一个函数来调用，示例如下：
```
alias tcstart='new() { /root/bin/tc-single-start "$1"; /root/bin/tclog "$1"; }; new'

alias pod1='podcmd() { echo $1; awk -v rst=$1 -v cmd="$*" "/^TN/{ gsub(/update/,\"\", \$0);print \$0 cmd}" ../README.MD;}; podcmd install'

alias pod1='podcmd() { echo $1; awk -v rst=$1 -v cmd="$*" "/^TN/{ gsub(/update/,cmd, \$0);print \$0; system("\$0")}" ../README.MD;}; podcmd install'
```

其中注意：`{`和`/root/bin/tc-single-start`之间要有空格，`"$1";`和`}`之间要有分号，函数末尾也要有分号。



