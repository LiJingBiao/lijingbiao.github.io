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

## bind支持传参

JavaScript 的 bind 方法不仅能绑定 this 指向,还可以绑定函数的参数。

bind 在绑定函数时,可以接受额外的参数,这些参数会被置于实际调用时的参数之前传给绑定函数。

举个例子:

```js
function add(a, b) {
  return a + b;
}

const add10 = add.bind(null, 10); 

add10(20); // 输出 30
```

上面代码中,我们通过 bind 把 add 函数的第一个参数绑定成 10。

调用 add10 时,其实就是调用 add 函数,只是第一个参数被绑定成 10 了。

再看一个例子:

```js
function greet(greeting, name) {
  console.log(greeting + ' ' + name);
}

const sayHello = greet.bind(null, 'Hello');

sayHello('John'); // 输出 Hello John
```

bind 可以绑定多个参数,被绑定的参数会按顺序排在实参之前传入原函数。

需要注意的是:

- bind 绑定的参数不能被后续调用的参数覆盖
- 如果绑定的参数比原函数参数数量多,多余的参数会被忽略

所以 bind 方法很适合用于参数柯里化,可以提前绑定一些参数,获得另一个更特定的函数。

## 多个样式使用数组

```
 <Text style={[styles.text, styles.header]}>
      根节点上放一个元素，不设置宽度
  </Text>   
```

## 样式可以不使用`StyleSheet.create`创建，直接使用对象创建

```react
styles = {
        circle: {
            backgroundColor: '#fe0000',
            borderRadius: 10,
            width: 20,
            height: 20
        }
    }
render3() {
        return (<View style={{ flex: 1, height: 100,width:300, backgroundColor: '#FA8072' }}>
            <View style={[this.styles.circle, { position: 'absolute', top: 50, left: 180 }]}>
            </View>
        </View>)

    }
```

## 使用`flex`布局，如果设置`flex=1`在主轴方向如果只有一个子view会默认充满,且在主轴方向的`长度`会失效

##  `View`如何什么不设置是不显示的,如果有子元素，且不设置宽、高，宽充满次轴方向，高为子元素高度，如果设置了就显示设置宽高

## 默认是相对定位，如果子组件使用了绝对定位，这个元素在子元素的flex布局就失效了

```react
 render3() {
        return (<View style={{ flex: 1, height: 100, backgroundColor: '#FA8072',flexDirection:'row',alignItems:'center',justifyContent:'space-around' }}>
            <View style={[this.styles.circle, { position: 'absolute', bottom: 50, left: 18 }]}>
            </View>
            <View style={[this.styles.circle, { }]}>
            </View>
            <View style={[this.styles.circle, {  }]}>
            </View>
            <View style={[this.styles.circle, {  }]}>
            </View>
        </View>)
```

## [react-native 之布局篇](https://segmentfault.com/a/1190000002658374)
