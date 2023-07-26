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

## `ES6`类可以直接调用实例方法

在 ES6 中,类的实例方法和类方法(静态方法)定义方式如下:

**实例方法**是定义在类的prototype属性上,需要通过实例调用:

```js
class Person {
  constructor(name) {
    this.name = name;
  }

  // 实例方法
  sayName() {
    console.log(this.name);
  }
}

const p = new Person('Jack');
p.sayName(); // Jack
```

sayName()就是一个实例方法,只能通过Person的实例来调用。

**类方法**(静态方法)是定义在类本身上的,可以直接通过类名调用:

```js 
class Person {
  constructor(name) {
    this.name = name;
  }
  
  // 类方法
  static create(name) {
    return new Person(name); 
  }
}

const p = Person.create('Jack');
```

create()就是一个静态方法,直接定义在Person类上,不需要实例就可以调用。

实例方法在原型对象(Person.prototype)上,类方法在类本身(Person)上。

需要注意的是,实例方法可以通过类名调用,但类方法不能通过实例调用。

总结:

- 定义在prototype上的是实例方法
- 定义在类本身上的都是类方法
- 实例方法可以通过实例和类名调用
- 类方法只能通过类名调用

## `AppState`可以监听设备的前后状态

## `useState`、`useRef`、`useEffect`的理解

在 React Native 中,useRef、useState 和 useEffect 都是常用的 Hooks,作用如下:

- useRef: 获取 DOM 元素或者组件的引用

```jsx
const myRef = useRef(null);

<View ref={myRef} />
```

useRef 可以用来保存组件内需要被持续引用的变量。

- useState: 定义状态变量并实现组件重新渲染

```jsx 
const [count, setCount] = useState(0);
```

useState 用来定义组件的状态变量,并返回当前状态值和更新状态的函数。

- useEffect: 处理副作用逻辑

```jsx
useEffect(() => {
  // 比如发起网络请求
}, []); 
```

useEffect 用来处理初始化逻辑、订阅逻辑等副作用函数,相当于 componentDidMount/componentDidUpdate/componentWillUnmount 的组合。

上述三个 Hooks 在 React Native 中使用方式与 React 一致,都是函数组件实现响应式逻辑的重要方式。具体来说:

- useRef 获取对组件内部元素的引用
- useState 定义状态变量
- useEffect 处理副作用逻辑

它们通常组合使用来实现复杂的组件逻辑。

------

React Hook 中 useEffect 的常见使用方式如下:

**执行副作用(发请求,手动变更 DOM 等)**

```jsx
useEffect(() => {
  // 发请求获取数据
  fetchData();
  
  // 更新文档标题
  document.title = `You clicked ${count} times`;
}, [count]); // 仅在 count 更改时重新执行
```

**模拟 componentDidMount 和 componentDidUpdate**

```jsx
useEffect(() => {
  // 调用 API 获取用户数据
}, []); // 空数组表示仅在组件挂载时执行
```

**模拟 componentWillUnmount** 

```jsx
useEffect(() => {
  // 订阅
  const subscription = props.source.subscribe();

  // 清除
  return () => {
    subscription.unsubscribe();
  };
}, [props.source]);
```

**性能优化(避免不必要的重渲染)**

```jsx
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
```

**引用上一轮的 props 或 state**

```jsx
function Counter() {
  const [count, setCount] = useState(0);

  const prevCountRef = useRef();
  useEffect(() => {
    prevCountRef.current = count; 
  })

  const prevCount = prevCountRef.current;
}
```

总结起来,useEffect 主要用于处理初始化逻辑、响应状态变化、清除订阅等副作用场景,配合其他 Hooks 可以实现强大的功能。

------

useEffect 的最后一个参数是数组,它允许我们优化 effect 的执行次数,避免不必要的重渲染。

这个数组参数有几种典型用法:

**1. 空数组**

```jsx
useEffect(() => {
  // 仅在组件挂载/卸载时执行
}, []); 
```

这种用法等价于 componentDidMount 和 componentWillUnmount,effect 不会在重新渲染时执行。

**2. 监听特定状态**

```jsx
useEffect(() => {
  // count 更改时执行
}, [count]);
```

这样可以仅在 count 状态发生改变时才执行 effect。

**3. 监听 props** 

```jsx
useEffect(() => {
  // 当 propName 发生变化时执行
}, [props.propName]); 
```

这样可以在 propName 变化时触发 effect。

**4. 全部列出**

```jsx
useEffect(() => {
  // 在组件初始化和任何状态改变时执行
}, [count, otherState, props.propName]); 
```

当需要在每次重新渲染时都执行 effect,可以传入所有相关的状态和 props。

总之,第二个参数允许我们性能优化,避免不必要的重渲染,只在关心的状态发生变化时重新执行 effect。



## 结构类里面的所有值

```js
const {page, pagesize, ...others} = this.state.params;
```

## `flex`布局

- [Flex 布局教程：语法篇](http://www.ruanyifeng.com/blog/2015/07/flex-grammar.html)

- [Flex 布局教程：实例篇](http://www.ruanyifeng.com/blog/2015/07/flex-examples.html)

## 运行iOS工程报错，找不到node环境

```
[Warning] You need to configure your node path in the `".xcode.env" file` environment.  You can set it up quickly by running:  `echo export NODE_BINARY=$(command -v node) > .xcode.env`  in the ios folder. This is needed by React Native to work correctly.  We fallback to the DEPRECATED behavior of finding `node`. This will be REMOVED in a future version.  You can read more about this here: https://reactnative.dev/docs/environment-setup#optional-configuring-your-environment
[Error] Could not find node. It looks like that the .xcode.env or .xcode.env.local 
Command PhaseScriptExecution failed with a nonzero exit code

```

解决办法

- 第一种办法

如果本地有`/usr/local/bin`目录

```
ln -s $(which node) /usr/local/bin/node
```

如果没有`/usr/local/bin`目录，创建一个

```
sudo mkdir /usr/local/bin
```

- 第二种办法

  找到node目录

  ```
  which node
  ```

  在xcode中设置

  ```
  export NODE_BINARY=[your node path]
  ../node_modules/react-native/packager/react-native-xcode.sh to node_modules/react-native/scripts/react-native-xcode.sh
  ```

  ![图片](https://i.stack.imgur.com/pwWA2.png)

- 第三种方法

  ```js
  # Fix for machines using nvm
  if [[ -s "$HOME/.nvm/nvm.sh" ]]; then
  . "$HOME/.nvm/nvm.sh"
  elif [[ -x "$(command -v brew)" && -s "$(brew --prefix nvm)/nvm.sh" ]]; then
  . "$(brew --prefix nvm)/nvm.sh"
  fi
  ```

[参考链接](https://stackoverflow.com/questions/44492197/react-native-ios-build-cant-find-node)

## 定义默认传参`Props`

```react
import PropTypes from 'prop-types';
export default class MyComponent extends Component {
	//类型
  static propTypes = {
    ...Text.propTypes,
    type: PropTypes.oneOf(['default', 'title', 'detail', 'danger']),
    size: PropTypes.oneOf(['xl', 'lg', 'md', 'sm', 'xs']),
    text: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
  };

  static defaultProps = {
    ...Text.defaultProps,
    type: 'default',
    size: 'md',
    numberOfLines: 1,
  };
}
```







