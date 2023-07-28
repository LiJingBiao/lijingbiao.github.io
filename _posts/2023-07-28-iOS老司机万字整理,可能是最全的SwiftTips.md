---
layout: post
title: iOS老司机万字整理, 可能是最全的Swift Tips  
date: 2023-07-28
tags: iOS
---
本文转自[iOS老司机万字整理, 可能是最全的Swift Tips  ](https://juejin.cn/post/7146890801207836703)

# 可能是最全的Swift Tips

## 1. 关于Swift

### 1.1 Swift的优点

1. Swft更加安全, 它是类型安全的语言.
2. Swift容易阅读, 语法和文件结构简易化.
3. Swift易于维护, 文件分离后结构更清晰.
4. Swift代码更少, 简洁的语法, 可以省去大量冗余代码.
5. Swift速度更快, 运算性能更高.

### 1.2 Swift和OC如何相互调用?

- Swift调用OC代码, 需要创建一个`Target-Bridging-Header.h`的桥接文件, 在桥接文件导入需要调用的OC代码头文件即可.
- OC调用Swift代码, 直接导入`项目名-Swift.h`文件即可, Swift如果需要被OC调用, 需要使用`@objc`对方法或者属性进行修饰.

### 1.3 Swift是面向对象编程(Object Oriented Programing)还是函数式编程(Functional programming)?

- Swift是一种混合编程语言, 它包含着两种编程模式.
- 它实现了面向对象的三个基本原则: **封装、继承、多态**.
- 函数式编程语言是指: **它是一种编程范式, 它将电脑运算视为函数计算, 并且避免使用程序状态以及易变对象.** 很难说Swift是一个成熟的函数式编程语言, 但是它已经具备了函数式编程语言的基础.

## 2. 基操知识点

### 2.1 Swift中struct和class的区别, struct能继承吗(不能)

- 在Swift中, class是引用类型(指针类型), struct是值类型.

#### **值类型**

1. 值类型在传递和赋值时将进行复制; 赋值给var、let或者给函数传参, 是直接将所有内容拷贝一份, 类似于对文件进行copy、paste操作, 产生了全新的文件副本. 属于深拷贝.
2. 值类型: 比如结构体, 枚举, 是在栈空间上存储和操作的.

#### **引用类型**

1. 引用类型只会使用引用对象的一个"指向"; 赋值给var、let或者给函数传参, 是将内存地址拷贝一份, 类似于制作一个文件的替身(快捷方式、链接), 指向的是同一个文件. 属于浅拷贝.
2. 引用类型: 比如Class, 是在堆空间上存储和操作的.

#### class和struct比较, 优缺点

class有以下功能, struct是没有的:

1. class可以继承, 子类可以使用父类的特性和方法
2. 类型转换可以在运行时检查和解释一个实例对象
3. class可以用deinit来释放资源
4. 一个类可以被多次引用

- 类中的每一个成员变量都必须被初始化, 否则编译器会报错, 而结构体不写.., 编译器会自动帮我们生成init函数, 给一个变量赋一个默认值

struct优势:

1. 结构较小, 适用于复制操作, 相比较一个class实例被多次引用, struct更安全
2. 无须担心内存泄漏问题

#### 2.1.1 在Swift中, 什么时候用`struct`, 什么时候用`class`?

- 函数式编程倾向于 **struct** , 面向对象编程更倾向于 **class**. 在Swift中, 类和结构体有许多不同的特性如下:

1. 类支持继承, 结构体不支持.
2. 类是引用类型, 结构体是值类型.

- 没有通用的规则决定结构体和类哪一个更好用, 一般的建议是使用最小的工具来完成你的目标.
- 但是有一个好的经验是 **多使用struct** , 除非你用了继承和引用语义.
- 在运行时, 结构体在性能方面更优于类, 原因是 **结构体的方法调用是静态绑定的** , 而 **类的方法调用是动态实现的**. 这就是尽可能使用结构体代替类的一个重要原因之一.

#### 2.1.2 Swift为什么将String、Array、Dictionary设计为值类型?

- 值类型和引用类型相比, **最大的优势是可以高效的使用内存.**
- 值类型在栈上操作, 引用类型在堆上操作, 栈上操作仅仅是单个指针的移动.
- 堆上操作涉及到内存的合并、位移、重链接.
- Swfit这样设计减少了堆上内存分配和回收次数, 使用写时复制(Copy-On-Write)将值传递与复制开销降到最低.

### 2.2 Swift中Class的内部实现和内存管理

### 2.3 文件访问权限关键字 private public

#### 2.3.1 访问级别

1. `open`

- open的权限是最大的, 可以在允许的实体模块、其它模块中访问, 并且允许其它模块进行继承和重写.
- 例如: TargetA中有classA, 权限是open, TargetB中的classB即可以继承classA, classA的方法, 成员变量等也可以被访问. ![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c97826f6265e48efbd6910300787798f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?)

1. `public`

- public和open是差不多的, 也是允许在实体模块, 其它模块中访问, 有一点区别是, 并不允许其它模块进行继承和重写.
- 例如: TargetA中有classA, 方法是testA, 权限是public, TargetB中有classB, 那么在classB中testB方法, 就可以初始化var a = classA(), 并且调用a.testA.

1. `internal`

- internal只允许在定义的实体模块进行访问, 不允许在其它模块中访问. 这个也是很多实体默认的权限.

1. `fileprivate`

- fileprivate翻译过来就是文件私隐, 它只允许在定义的文件中访问.
- 例如: 在一个Target中, 有classA和classB两个类分别在两个文件, classA当前权限是fileprivate, 那么classB是不能访问classA的. 如果classA和classB是在同一个文件下, 就可以访问.

1. `private`

- private只允许在当前定义实体中访问.
- 例如: classA和classB都在同一个文件, classA的权限是private, 那么classB原则上是不能访问classA的. 要访问的话, 需要一些情况.

#### 2.3.2 访问级别的使用准则

- 一个实体不可以被更低的访问级别的实体定义.

1. 变量类型的访问级别 \>= 变量的访问级别

- 例如: 定义一个类`fileprivate class ClassA{}`, 如果定义为`internal var classA: ClassA`就会报错, 权限ClassA的试题类型需要大于变量classA.

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee00da0c311741238f4187d8774f170d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?)

1. 参数类型, 返回值类型 \>= 函数

- 例如: `func testA(_ num: Int) -> Double{}`, 函数的访问级别默认是`internal`, 参数的num是`public`, 返回值Double也是`public`

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6a1bb075b76480d861a0671fb723490~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?)

1. 父类 \>= 子类

- 相当于说我能访问子类, 那么父类也应该要可以访问才对.
- 例如: `class SupClassA{}`, 子类`class ClassA: SupClassA{}`, 父类的默认全显示`internal`, 那么子类就不能为`public`和`open` ![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d48dd93552f64fca9959467e8b285472~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?)

#### 2.3.3 成员嵌套类型

1. 类型为`private, fileprivate`

- 当前类型为`private, fileprivate`, 那么成员的默认类型也是`private`或`fileprivate`
- 例如: `fileprivate class ClassA { var a = 0, var b = 0}`, a和b默认都是`fileprivate`

1. 类型为`internal, public`

- 当类型为`internal, public`, 成员的默认类型为internal

```
public class ClassA {
    internal var a = 0
}
复制代码
```

#### 2.3.4 **直接在全局作用域下定义的`private`等价于`fileprivate`**

1. 可以编译通过 ![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fb1ed60cb2e4d1a93d5ecb12952476c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?)
2. 不可以编译通过 ![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1928e34d7d494ee1b70c2c05e3472e1b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?)

#### 3.4 getter, setter权限

- 对于读写方面, 很多时候我们希望别人读我们的值, 而不允许修改我们的值, 我们可以这么定义如下:

```
class ClassA {
    private(set) var age: Int = 0
}
复制代码
```

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f6df2de87b44b13a6399a0c5a98b186~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?)

### 2.4 Swift的module的默认访问权限, module内部的访问权限

### 2.5 写时复制机制, OC中类似的机制是什么?

值类型(比如struct), 在复制时, 复制对象与原对象实际上在内存中指向同一个对象, 当且仅当修改复制的对象时, 才会在内存中创建一个新的对象.

1. 为了提升性能, 值类型:struct, enum, Int, Double, Float, String, Array, Dictionary、Set采取了Copy On Write的技术
2. 比如仅当有"写"操作时, 才会真正执行拷贝操作
3. 对于标准库值类型的赋值操作, Swift能确保最佳性能, 所以没必要为了保证性能来避免赋值

```
let array = [1, 2, 3]
var array1 = array

// 断点1, 此时array和array2内存地址一致
array1 = array
// 断点2, 此时array和array2内存地址不一致
复制代码
```

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3e4814504b1429a9f4b4012c9435b96~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?)

- 写时复制允许共享同一个内存地址, 直到其中之一发生改变. 这样的设计使得值类型可以被多次复制而无需消耗多余的内存, 只有在变化的时候才会增加开销, 隐藏内存的使用更加高效.

- 在OC语言中, 想要获取多个完全一致、互不干扰的对象, 可以使用mutableCopy.

```
NSMutableArray *array = [NSMutableArray arrayWithObjects:@1, @2, @3, nil];
NSMutableArray *array1 = [array mutableCopy];
复制代码
```

### 2.6 什么是`optional`类型, 它是用来解决什么问题的?

- `optional`类型被用来表示任何类型的变量的 **缺少值**. 在OC中, 引用类型的变量是可以缺失值, 并且使用`nil`作为缺少值. 基本数据类型没有这种功能.
- Swift用`optional`扩展了在基本数据类型和引用类型中 **缺少值** 的概念, 一个`optional`类型的变量, 在任何时候都可以 **保存一个值** 或者为`nil`.

### 2.7 什么是泛型? 泛型是用来解决什么问题的?

- 泛型是让你能根据自定义的需求, 编写出适用于任意类型的、灵活可复用的函数及类型. 你可以避免编写重复的代码, 而是用一种清晰抽象的方式来表达代码的意图.

#### 2.7.1 Swift中泛型的高级使用

- Swift包含 **泛型类** 和 **泛型结构体** , 泛型可以在类、结构体、枚举、全局函数或者方法中使用.
- **泛型协议** 是通过`typealias`部分实现的, `typealias`不是一个泛型类型, 他只是一个 **占位符的名字**. 它通常是作为关联类型被引用, 只有协议被一个类型引用的时候它才被定义.

### 2.8 哪些情况下使用隐式解包?

- 对`optional`变量使用隐式解包最常见的原因如下:

1. 对象的属性在初始化的时候不能为`nil`, 否则不能初始化成功. 典型的例子是`Interface Builder outlet`类型的属性, 它总是在它的拥有者初始化之后再初始化. 在这种特定的情况下, 假设他在`Interface Builder`中被正确的配置--`outlet`被使用之前, 保证它不为`nil`.
2. 解决强引用的循环问题, 当两个实例对象相互引用, 并且对引用的实例对象的值要求不能为`nil`时候. 在这种情况下, 引用的一方可以标记为`unowned`, 另一方使用隐式解包.
3. 除非必要, 否则尽量不要对`optional`类型使用隐式解包. 使用不当会增加运行时crash的可能性.在某些情况下, crash可能是有意的行为, 但这种情况更推荐`fatalError()`函数.

#### 2.8.1 对一个`optional`变量解包有哪些方法?

1. 强制解包, `!`操作符, 不安全,容易引起运行时崩溃.
2. 隐式解包, 在变量声明时, 大多数情况也不安全, 也有可能引起运行时崩溃.
3. 可选绑定`if let`和`guard let`.
4. 自判断连接`optional chaining`.
5. 合并空值运算符`??`.
6. `guard`语句.
7. 可选模式`optional pattern`.

### 2.9 Swift中的常量定义和OC的区别

```
// 在OC中可以这样定义常量:
const int number = 0;

// 类似的Swift是这样定义的:
let number = 0
复制代码
```

- `const`常量是一个在编译时或者编译解析时被初始化的变量.
- 通过`let`创建的是一个运行时常量, 是不可变的. 它可以使用`static`或者`dynamic`关键字类初始化. 它的值只能被分配一次.

### 2.10 Swift中的`static`或者`class`修饰符的作用

- 声明一个静态属性或者函数, 我们常常使用值类型的`static`修饰符. 下面就是一个结构体的例子:

```
struct Sun {
    static fun illuminate() {}
}
复制代码
```

- 对类来说, 使用`static`或者`class`修饰符, 都是可以的. 他们使用后的效果是一样的, 但是本质上是不同的.
- 本质不同原因是: `static`修饰的属性或者修饰的函数都不可以重写. 但是使用`class`修饰符, 你可以重写属性或者函数.
- 当`static`在类中应用的时候, `static`就成为`class final`的一个别名.
- 例如下面代码中, 当你尝试重写`illuminate()`函数的时候, 编译器就会报错:

```
class Star {
    class func spin() {}
    static func illuminate() {}
}

class Sun : Star {
    override class func spin() {
        super.spin()
    }
    override static func illuminate() { // error: Cannot override static method
        super.illuminate()
    }
}
复制代码
```

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fe5990641734c2782b1396f51168262~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?)

- 在`sil`代码中可以看到`class` 修饰的类方法存储在`VTable`中, `static`修饰的类方法是以静态方法的形式存储的.

### 2.11 Swift中能通过`extension`保存一个属性吗?

- 不能. `extension`可以给当前类型添加新的行为, 但不能改变本身的类型或者本身的接口.
- 如果你添加一个新的可存储的属性, 你需要额外的内存来存储新的值. 扩展不能实现这样的任务.

### 2.12 闭包是引用类型吗?

1. 闭包是一个引用类型.
2. 闭包捕获值的本质是在堆区开辟内存, 然后存储其在上下文中捕获到的值.
3. 修改值也是修改的堆空间的值.
4. 闭包的底层结构是一个结构体. 首先存储闭包的地址; 加上捕获值的地址.
5. 在捕获的值中, 会对定义的变量和函数中的参数分开存储.
6. 存储的时候内部会有一个`HeapObject`结构, 用于管理内存、引用计数
7. 函数是特殊的闭包, 只不过函数不捕获值, 所以在闭包结构体中只存储 **函数地址** , 不存储指向捕获值的 **指针**.

### 2.13 如何把一个负整数转换成一个无符号的整数?

- `UInt`类型是用来存储无符号整型的. 下面的代码实现了一个有符号整型转换的初始化方法:`let myNegative = UInt(-1)`
- 我们知道负数的内部结构是使用二进制 **补码** 的正数, 在保持这个负数内存地址不变的情况下, 如何把一个负整数转换成一个无符号的整数?
- 原码: **原码就是符号位加上真值的绝对值, 即用第一个二进制位表示符号(正数该位为0, 负数该位为1), 其余位表示值.**
- 反码: 正数的反码与其原码相同; 负数的反码是对其原码逐位取反, 但符号位除外.
- 补码: 正数的补码就是其本身; 负数的补码是在其反码的基础上+1

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef21e2faa08a412eb886390e07cf2a6d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?)

### 2.14 描述一种在Swift中出现循环引用的情况.

- 循环引用出现在两个实例对象相互拥有强引用关系的时候, 这会造成内存泄漏, 原因是这两个对象都不会被释放, 只要一个对象被另一个对象强引用, 那么该对象就不能被释放, 由于强引用的存在, 每个对象都会保持对方存在.
- 解决办法可以使用`weak`或者`unowned`.
- 转换为值类型, 只有类会存在喧嚷引用, 如果能用把`class`换成`struct`, 是可以避免循环引用的.
- `delegate`使用`weak`属性.
- 闭包中, 对有可能发生循环引用的对象, 使用`weak`或者`unowned`修饰.

#### 2.14.1 关键字`strong、weak、unowned`的区别?

- Swfit的内存管理机制同OC一致, 都是ARC, `strong`和`weak`同OC一样.
- `unowned`(无主引用), 不会产生强引用, 实例销毁后仍然存储着实例的内存地址(类似于OC中的`unsafe_unretained`), 它仍然 **会保持对被已经释放了的对象的一个"无效的"引用, 它不是`Optional`, 也不会被指向`nil`,** 如果试图在实例销毁后访问无主引用`unowned`, 会产生运行时错误(悬垂指针).
- `weak`, 当我们赋值给一个被标记为`weak`的变量时, 它的引用计数不会被改变. 而且当这个弱引用变量所引用的对象被释放时, 这个变量将被自动设为`nil`. 这也是 **弱引用必须被声明为`Optional`的原因.**
- 在引用对象的生命周期内, **如果它可能为nil, 那么就用`weak`引用. 反之, 当你知道引用对象在初始化后永远都不会为nil, 就用`unowned`.**
- 如果你知道你引用的对象会在正确的时机释放掉, 且它们是相互依存的, 而你不想写一些多余的代码来情况你的引用指针, 那么你就应该使用`unowned`引用而不是`weak`引用.

```
class SwiftViewControllerA: UIViewController {

    var person : Person?

    override func viewDidLoad() {
        super.viewDidLoad()

        person = Person()

        person?.testClosure()

        person = nil
        
    }
}

// 测试unowned和weak

class SomeSigleton {

    static let share = SomeSigleton()

    func closure(closure: (() -> Void)?) {

        DispatchQueue.global().asyncAfter(deadline: .now() + 2) {
            closure?()
        }

    }

}

class Person {

    let someSigleton = SomeSigleton.share
    let portrait = UIImage()

    func testClosure() {

        someSigleton.closure { [unowned self] in
            print(self.portrait)
        }
        
        // 使用weak修饰就不会有问题!
        //        someSigleton.closure { [weak self] in
//            print(self?.portrait)
//        }

    }

    deinit {
        print("Person is deinited")
    }

}
复制代码
```

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c509e48b58d54aea9365482a17c59095~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?)

- Apple文档使用建议

```
Define a capture in a closure as an unowned reference when the closure and the instance it captures will always refer to each other, and will always be deallocated at the same time.

Conversely, define a capture as a weak reference when the captured reference may become nil at some point in the future. Weak references are always of an optional type, and automatically become nil when the instance they reference is deallocated. This enables you to check for their existence within the closure’s body.
复制代码
```

- 当我们知道两个对象的生命周期并不相关, 那么我们必须使用`weak`. 相反, 非强引用对象拥有和强引用对象同样或者更长的声明周期的话, 则应该使用`unowned`.
- 例如, `ViewController`对它的`SubView`的引用可以使用`unowned`. 因为`ViewController`的生命周期一定比它的`SubView`长. 而在使用服务时, 则需要看情况使用`weak`. 因为服务的初始化方法可能是被工厂模式或`Service Locator`所封装. 这些服务可能在某些时候被重构为单例, 此时它们的生命周期发生了改变.

### 2.15 什么关键字可以实现 **递归枚举**?

- `indirect`

```
enum List<T> {
    case end
    indirect case node(T, next: List<T>)
}

indirect enum List<T> {
    case end
    case node(T, next: List<T>)
}
复制代码
```

### 2.16 什么是属性观察?

- 属性观察是指在当前类型内对特性属性进行监测, 并做出相应. 属性观察是Swift中的特性, 具有两种方法, `willset`和`didset`

```
var title: String {
    willSet {
        print("willSet", newValue)
    }
    didSet {
        print("didSet", oldValue, title)
    }
}
复制代码
```

- `willSet`会传递新值, 默认叫`newValue`
- `didSet`会传递旧值, 默认叫`oldVlaue`
- 在初始化器中设置属性不会触发willSet和didSet

### 2.17 比较Swift和OC中的初始化方法`init`有什么不同?

- Swift的初始化方法, 更加严格和准确, Swift初始化方法需要保证所有的`非Optional`的成员变量都完成初始化, 同时Swift新增了`convenience`和`required`两个修饰初始化器的关键字.
- `convenience`只提供了一种 **便捷的初始化器** , 必须通过一个 **指定初始化器** 来完成初始化.
- `required`是强制子类重写父类中所修饰的初始化方法.

### 2.18比较Swift和OC中的`protocol`有什么异同?

- 相同点: 两者都可以被用作代理.
- 不同点: Swift中的`protocol`还可以对接口进行抽象, 可以实现面向协议编程, 从而大大提高编程效率; Swift中的`protocol`可以用于值类型、结构体、枚举.

#### 2.18.1 如何将Swift中协议`protocol`中的部分方法设计为可选`Optional`?

- 在协议和方法前面添加`@objc`, 然后在方法前面添加`optional`关键字, 该方式实际上是将协议转为了OC的方式.

```
@objc protocol someProtocol {
    @objc optional func testProtocol()
}
复制代码
```

- 使用扩展`extension`, 来规定可选方法, 在Swfit中, 协议扩展可以定义部分方法的默认实现

```
protocol someProtocol {
    func test()
}

extension someProtocol {
    func test() {
        print("test")
    }
}
复制代码
```

#### 2.19 Swift和OC中的自省方法有什么区别?

- OC中的自省方法就是判断某一个对象是否属于某一个类的操作, 有以下2种方式

```
// 判断obj是否是某个类
[obj isKindOfClass:[SomeClass class]];

// 判断obj是否是某个类或者是该类的子类
[obj isMemberOfClass:[SomeClass class]];
复制代码
```

- 在Swift中由于很多`class`并非继承自`NSObject`, 故而Swift使用`is`来判断是否属于某一类型, `is`不仅可以作用于`class`, 还能作用于`enum`和`struct`.

### 2.20 什么是函数重载? Swift支持函数重载吗?

- 函数重载: 函数名相同, 函数的参数个数不同, 或者参数类型不同, 或参数标签不同, 返回值类型与函数重载无关.
- Swift支持函数重载.

### 2.21 Swift中枚举的\ ***关联值** 和 **原始值** 的区分?

- **关联值** : 有时会将枚举的成员值跟其他类型的变量关联存储在一起, 会非常有用.

```
// 关联值
enum Date {
    case digit(year: Int, month: Int, day: Int)
    case string(String)
}
复制代码
```

- **原始值** : 枚举成员可以使用相同类型的默认值预先关联, 这个默认值叫做: 原始值.

```
// 原始值
enum Grade: String {
    case perfect = "A"
    case great = "B"
    case good = "C"
    case bad = "D"
}
复制代码
```

### 2.22 Swift中的闭包 **Closure** 相关

#### 2.22.1 Swift中的闭包结构是什么样的?

```
{
    (参数列表) -> 返回值类型 in 函数体代码
}
复制代码
```

#### 2.22.2 什么是尾随闭包?

- 将一个很长的闭包表达式作为 **函数的最后一个实参**.
- 使用尾随闭包可以增强函数的 **可读性**.
- 尾随闭包是一个被书写在函数调用括号外面(后面)的闭包表达式.

```
// fn就是一个尾随闭包参数
func exec(v1: Int, v2: Int, fn: (Int, Int) -> Int) {
    print(fn(v1, v2))
}

// 调用
exec(v1: 10, v2: 20) {
    $0 + $1
}
复制代码
```

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76247b3bdb124edcaf4256aeb3f51f92~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?)

#### 2.22.3 什么是逃逸闭包?

- 当闭包作为一个实际参数传递给一个函数或者变量的时候, 我们就说这个闭包逃逸了, 可以在形式参数前写`@escaping`来明确闭包是允许逃逸的.
- 非逃逸闭包、逃逸闭包, 一般都是当做参数传递给函数.
- 非逃逸闭包: 闭包调用发生在函数结束前, 闭包调用在函数作用域内.
- 逃逸闭包: 闭包有可能在函数结束后调用, **闭包调用逃逸出了** 函数的 **作用域** , 需要通过 `@escaping`声明.

```
// 定义一个数组用于存储闭包类型
var completionHandlers: [() -> Void] = []

// 在方法中将闭包当做实际参数, 存储到外部变量中
func someFunctionWithEscapingClosure(completionHandler: @escaping () -> Void) {
    completionHandlers.append(completionHandler)
}
复制代码
```

- **上面这种情况, 如果不标记函数的形式参数为`escaping`, 就会编译报错.**

#### 2.22.4 什么是自动闭包?

- 自动闭包是一种 **自动创建的用来把作为实际参数传递给函数的表达式打包的闭包**.
- 它不接受任何实际参数, 并且当它被调用时, 它会返回内部打包的表达式的值.
- 这个语法的好处在于通过写普通表达式 **代替显式闭包而使你省略包围函数形式参数的括号.**

```
func getFirstPositive(_ v1: Int, _ v2: @autoclosure () -> Int) -> Int? {
    return v1 > 0 ? v1 : v2()
}
getFirstPositive(10, 20)
复制代码
```

- 为了避免与期望冲突, 使用了`@autoclosure`的地方最好明确注释清楚: **这个值会被推迟执行.**
- `@autoclosure`会自动将20封装成闭包`{ 20 }`
- `@autoclosure`只支持`()->T`格式的参数
- `@autoclosure`并非只支持最后一个参数
- 有`@autoclosure`、无`@autoclosure`, 构成了 **函数重载**.

### 2.23 合并空值运算符 `??`

- `a ?? b`
- a 是可选项, b 可以是可选项也可以不是可选项, b跟a的存储类型必须相同.
- 如果a不为`nil`, 就返回a.
- 如果a为`nil`, 就返回b. 如果b不是可选项, 返回a时, 会对a进行自动解包操作.

```
let a: Int? = 1
let b: = 2

// 此时c为Int型, 不是可选类型. 而且值为1.
let c = a ?? b // 
复制代码
```

- 所以`??`返回的类型取决于b.

```
public func ?? <T>(optional: T?, defaultValue: @autoclosure () throws -> T) rethrows -> T

public func ?? <T>(optional: T?, defaultValue: @autoclosure () throws -> T?) rethrows -> T?
复制代码
```

- **从上面的定义就可以看出来.**

### 2.24 Swfit中, 存储属性和计算属性的区别?

- Swfit中跟实例对象相关的属性可以分为两大类

1. **存储属性(Stored Property)**

- 类似于成员变量这个概念
- 存储在实例对象的内存中
- 结构体、类可以定义存储属性
- 枚举不可以定义存储属性

1. **计算属性(Computed Property)**

- 本质就是方法(函数)
- 不占用实例对象的内存
- 枚举、结构体、类都可以定义计算属性

```
struct Circle {
    // 存储属性
    var radius: Double
    
    //计算属性
    var diameter: Double {
        set {
            radius = newValue / 2
        }
        get {
            return radius * 2
        }
    }
}
复制代码
```

#### 2.24.1 什么是延迟存储属性(Lazy Stored Property)?

- 使用`lazy`可以定义一个延迟存储属性, 在第一次用到属性的时候才会进行初始化(类似OC中的懒加载).
- `lazy`属性必须是`var`, 不能是`let`(`let`必须在实例对象的初始化方法完成之前就拥有值).
- 如果多条线程同时第一次访问`lazy`属性, 无法保证属性只被初始化一次.

```
class PhotoView {
    // 延迟存储属性
    lazy var image: Image = {
        let url = "http://www.baidu.com...png"
        let data Data(url: url)
        return Image(data: data)
    }()
}
复制代码
```

#### 2.24.2 什么是属性观察器?

- 可以为非`lazy`的`var`存储属性设置属性观察器, 通过关键字`willset`和`didset`来监听属性变化.

```
struct Circle {
    var radius: Double {
        willSet {
            print("willSet", newValue)
        }
        didSet {
            print("didSet", oldValue, radius)
        }
    }
    
    init() {
        self.radius = 1.0
        print("Circle init!")
    }
}
复制代码
```

#### 2.24.3 Swift中什么是类型属性(Type Property)?

- 严格的说, 属性可以分为

- 实例属性(Instance Property): 只能通过实例对象去访问.

- 
  - 存储实例属性(Stored Instance Property): 存储在实例对象的内存中, 每个实例对象都有一份.
- 
  - 计算实例属性(Computed Instance Property)
- 类型属性(Type Property): 只能通过类型去访问

- 
  - 存储类型属性(Stored Type Property): 整个程序运行过程中, 就只有一份内存(类似于全局变量).
- 
  - 计算类型属性(Computed Type Property)
- 可以通过`static`定义类型属性p如果是类, 也可以用关键字`class`.

```
struct Car {
    static var count: Int = 0
    init() {
        Car.count += 1
    }
}
复制代码
```

- 不同于存储实例属性, 你必须给存储类型属性设定初始值.
- 
  - 因为类型没有像实例对象那样的`init`初始化器来初始化存储属性.
- 存储属性默认就是`lazy`, 会在第一次使用的时候才初始化.
- 
  - 就算被多个线程同时访问, 保证只会初始化一次.
- 
  - 存储类型属性可以是`let`.
- 枚举类型也可以定义类型属性(存储类型属性、计算类型属性)

### 2.25 Swfit中如何使用单例模式?

- 可以通过`类型属性 + let + private`来写单例, 代码如下:

```
public class FileManager {
    public static let shared = {
        ...
        return FileManager()
    }
    
    private init() {}
}
复制代码
```

### 2.26 Swfit中的下标是什么?

- 使用`subscript`可以给任意类型(枚举、结构体、类)增加下标功能, 有些地方也翻译为: 下标脚本.
- `subscript`的语法类似于实例方法、计算属性, 本质就是方法(函数). 使用如下:

```
class Point {
    var x = 0.0, y = 0.0
    
    subscript(index: Int) -> Double {
        set {
            if index == 0 {
                x = newValue
            } else if index == 1 {
                y = newValue
            }
        }
        get {
            if index == 0 {
                return x
            } else if index == 1 {
                return y
            }
            return 0
        }
    }
}

var p = Point()

// 下标值
p[0] = 11.1
p[1] = 22.2

// 下标访问
print(p.x)// 11.1
print(p.y)// 22.2
复制代码
```

### 2.27 简单说一下Swift中的初始化器

- 类、结构体、枚举都可以定义初始化器
- 类有两种初始化器: 指定初始化器`designated initializer`、便捷初始化器`convenience initializer`

```
// 指定初始化器
init(parameters) {
    statements
}

// 便捷初始化器
convenience init(parameters) {
    statements
}
复制代码
```

**规则:**

- 每一个类至少有一个指定初始化器, 指定初始化器是类的主要初始化器
- 默认初始化器总是类的指定初始化器
- 类偏向少量指定初始化器, 一个类通常只有一个指定初始化器

**初始化器的相互调用规则**

- 指定初始化器必须从它的直系父类调用指定初始化器
- 便捷初始化器必须从相同的类里调用另一个初始化器
- 便捷初始化器最终必须调用一个指定初始化器

### 2.28 什么是可选链?

- 可选链是一个调用和查询可选类型、方法和下标的过程, 它可能为`nil`.
- 如果可选项包含值, 那么属性、方法或者下标的调用成功;
- 如果可选项是`nil`, 属性、方法或者下标的调用会返回`nil`.
- 多个查询可以链接在一起, 如果链中任何一个节点是`nil`, 那么整个链就会得体的失败.

### 2.29 什么是运算符重载(Operator Overload)?

- 类、结构体、枚举可以为现有的运算符提供自定义的实现, 这个操作叫: **运算符重载**.

```
struct Point {
    var x: Int
    var y: Int
    
    // 运算符重载
    static func + (p1: Point, p2: Point) -> Point {
        return Point(x: p1.x + p2.x, y: p1.y + p2.y)
    }
}

var p1 = Point(x: 10, y: 10)
var p2 = Point(x: 20, y: 20)
var p3 = p1 + p2
复制代码
```

## 3. OC和Swift运行时简介

### 3.1 Objective-C运行时

- 动态类型 (dynamic typing)
- 动态绑定 (dynamic binding)
- 动态装载 (dynamic loading)

#### 3.1.1 OC对象调用方法的过程

- `[object methodA]`

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61d0dc76b186478e9e4644cfd7d1bc8e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?)

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80cf8816cdd14475a99fbaff12949fef~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?)

### 3.2 派发方式

#### 3.2.1 直接派发 (Direct Dispatch)

- 直接派发是最快的, 不止是因为需要调用的指令集会更少, 并且编译器还能够有很大的优化空间, 例如函数内联等, 直接派发也有人称为静态调用.
- 然而, 对于编程来说直接调用也是最大的局限, 而且因为缺乏动态性所以没办法支持 **继承** 和 **多态**.

#### 3.2.2 函数表派发 (Table Dispatch)

- 函数表派发是编译型语言实现动态行为最常见的实现方式. 函数表使用了一个数组来存储类声明的每一个函数的指针. 大部分语言把这个称为"Virtual table(虚函数表)", Swift里称为 **"witness table"**. 每一个类都会维护一个函数表, 里面记录着类所有的函数, 如果父类函数被override的话, 表里面只会保存被override之后的函数. 一个子类新添加的函数, 都会被插入到这个数组的最后. 运行时会根据这一个表去决定实际要被调用的函数.

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3654488ad411455680c13aecd9b2a596~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?)

- 查表是一种简单、易实现, 而且性能可预知的方式. 然而, 这种派发方式比起直接派发还是慢一点. 从字节码角度来看, 多了两次读和一次跳转, 由此带来了性能的损耗. 另一个慢的原因在于编译器可能会由于函数内执行(如果函数带有副作用的话)的任务导致无法优化.
- 这种基于数组的实现, 缺陷在于函数表无法拓展. 子类会在虚数函数表的最后插入新的函数, 没有位置可以让extension安全地插入函数.

#### 3.2.3 消息机制派发 (Message Dispatch)

- 消息机制是调用函数最动态的方式. 也是Cocoa的基石, 这样的机制催生了KVO、UIAppearence和CoreData等功能. 这种运作方式的关键在于开发者可以在运行时改变函数的行为. 不止可以通过swizzling来改变, 甚至可以用isa-swizzling修改对象的继承关系, 可以在面向对象的基础上实现自定义派发.

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75a0375613e54949b5c06b71a385abc4~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?)

### 3.3 Swift运行时

- 纯Swift类的函数调用已经不再是Objective-C的运行时发消息, 而是类型C++的vtable, 在编译时就确定了调用哪个函数, 所以没法通过runtime获取方法、属性.
- 而Swift为了兼容Objective-C, 凡是继承自NSObject的类都会保留其动态性, 所以我们能通过runtime拿到他的方法. (老版本的Swift(如2.2)是编译期隐式的自动帮你加上了`@objc`, 而Swift4.0以后编译期去掉了隐式特性, 必须使用显示添加.)
- 不管是纯Swift类还是继承自NSObject的类, 只有在属性和方法前添加了`@objc`关键字就可以使用runtime.

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5dfeb3966fa346a082b79cabf3f049ff~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?)

- 值类型总是会使用直接派发, 简单易懂
- 协议和类的extension都会使用直接派发
- NSObject的extension会使用消息机制进行派发
- NSObject声明作用域里的函数都会使用函数表进行派发
- 协议里声明的, 并且带有默认实现的函数会使用函数表进行派发

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d56b5a94063407d87494ace9d3dac35~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?)

#### 3.3.1 Swift运行时-final @objc

- 可以在标记为`final`的同时, 也使用`@objc`来让函数可以使用消息机制派发. 这么做的结果就是, 调用函数的时候会使用直接派发, 但也会在Objective-C的运行时里注册相应的selector. 函数可以响应`perform(selector:)`以及别的Objective-C特性, 但在直接调用时又可以有直接派发的性能.


