---
layout: post
title: Ruby Ruby 里的 %Q, %q, %W, %w, %x, %r, %s, %i 
date: 2022-04-18
tags: ruby
---


# [Ruby](/topics/node1) Ruby 里的 %Q, %q, %W, %w, %x, %r, %s, %i (译) 



[原文地址](https://simpleror.wordpress.com/2009/03/15/q-q-w-w-x-r-s/)

## %Q

用于替代双引号的字符串. 当你需要在字符串里放入很多引号时候, 可以直接用下面方法而不需要在引号前逐个添加反斜杠 (\")

```
>> %Q(Joe said: "Frank said: "#{what_frank_said}"")
=> "Joe said: "Frank said: "Hello!"""
```

`(`...`)`也可用其他非数字字母的符号或成对的符号代替, 诸如`[`...`]`, `!`...`!`, `+`...`+`,`{`...`}`, `<`...`>`等.  
以下写法全部与上面等效:

```
>> %Q!Joe said: "Frank said: "#{what_frank_said}""!
>> %Q[Joe said: "Frank said: "#{what_frank_said}""]
>> %Q+Joe said: "Frank said: "#{what_frank_said}""+
```

除此之外还可省略`Q`写作:

```
>> %/Joe said: "Frank said: "#{what_frank_said}""/
=> "Joe said: "Frank said: "Hello!"""
```

## %q

与`%Q`类似, 但是表示的是单引号字符串

```
>> %q(Joe said: 'Frank said: '#{what_frank_said} ' ')
=> "Joe said: 'Frank said: '\#{what_frank_said} ' '"
```

## %W

语法近似于`%Q`, 用于表示其中元素被双引号括起的数组.

```
>> %W(#{foo} Bar Bar\ with\ space)
=> ["Foo", "Bar", "Bar with space"]
```

## %w

用于表示其中元素被单引号括起的数组. 比较奇怪的是`\`(斜杠空格) 会被转化成``(空格), 但是其他的内容不会.

```
>> %w(a b c\ d \#e #{1}f)
=> ["a", "b", "c d", "\\#e", "\#{1}f"]
```

## %x

使用`方法执行一段 shell 脚本并返回标准输出内容.

```
>> %x(echo foo:#{foo})
=> "foo:Foo\n"
```

## %r

语法近似于`%Q`, 用于正则表达式.

```
>> %r(/home/#{foo})
 => "/\\/home\\/Foo/"
```

## %s

用于表示 symbol, 但是不会对其中表达式等内容进行转化

```
>> %s(foo)
=> :foo
>> %s(foo bar)
=> :"foo bar"
>> %s(#{foo} bar)
=> :"\#{foo} bar"
```

## %i

Ruby 2.0 之后引入的语法, 用于生成一个 symbol 数组

```
2.0.0p247 :014 > %i(a b c)
=> [:a, :b, :c]
```

## %

还有% 操作符 [% 的用法（即 sprintf）](http://www.kuqin.com/rubycndocument/man/sprintf_format.html)

```
irb(main):125:0> '%02d' % 9
=> "09"
```

