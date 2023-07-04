---
layout: post
title: Swift 关于 module.modulemap 使用
date: 2023-07-04
tags: iOS
---



# Swift 关于 module.modulemap 使用

[原文](Swift 关于 module.modulemap 使用)

2020-7-12 更新：`为什么在 swift framework 中使用了自定义module.modulemap, build 出来的 framework 会报 Missing required module`  
受 [@Ulquiorra\_04](https://www.jianshu.com/u/4233cf28ea01) 的提醒，开始测试并写了这篇文章《[Swift Framework 自定义 Module](https://www.jianshu.com/p/b4f88651f069)》，介绍了如何实现在 swift framework 中使用自定义 module。

`Swift` 中最简单最优雅的引用 `oc` 和 `c` 方式。  
首先建一个 `group`， 就是你要 `import` 的，如图文件名叫 `OtherFile`，所以在哪里要使用这个`module`的文件，就直接 `import OtherFile`。

```
// like this
import UIKit
import OtherFile

class ViewController: UIViewController {
    override func viewDidLoad() {
        ...
    }
}
```

![](/images/posts/iOS/swiftmodule/swift_module_2.jpg)

module.modulemap 文件

```
// module.modulemap 文件
module OtherFile {
    // headers.h 和 module.modulemap 必须在同一group下，否则需要配置 `header "/??/headers.h"`
    header "headers.h"
    export *
}
```

headers.h文件

```
// headers.h文件
// 在 headers.h 中引用需要暴露的文件

// for c++
#include "file.h"
// for c
#include "file_c.h"

//#ifdef __OBJC__
// for oc
#import "Test.h"
#import "Test2.h"
//#endif
```

注意, 同时存在 `oc` 和 `c` 文件 需要分开处理, 需要把 oc 文件单独加上 `requires objc`, 所以建议使用 `umbrella`, 并且把 `c` 和 `oc` 分开多个 `module`.  
[requires 列表](https://links.jianshu.com/go?to=https%3A%2F%2Fclang.llvm.org%2Fdocs%2FModules.html%23requires-declaration)

```
module OtherFile {
    // c file
    header "file.h"
    header "filea.h"
    header "filebbb.h"
    
    export *
    umbrella "Subs"
    module * { export * }
    
    // oc file
    module Test {
        requires objc
        header "Test3.h"
        header "Test2.h"
        header "Test.h"
        export *
        
        export *
        umbrella "Subs/OCSubs" // 单独把 Subs 中的 oc 文件, 单独列出来, 否则会编译失败
        module * { export * }
    }
}
```

### The std module can be extended to also include C++ and C++11 headers using a requires-declaration:

```
module std {
   // C standard library...

   module vector {
     requires cplusplus
     header "vector"
   }

   module type_traits {
     requires cplusplus11
     header "type_traits"
   }
 }
```

同时需要配置如图

![](/images/posts/iOS/swiftmodule/swift_module_1.jpg)

`import paths` 通过语义就是 可以 `import` 的，即 `import OtherFile`。  
可以直接拖拽 `group` 直接到目录下, 需要配置 `$SRCROOT/`, 绝对路径。  
之后就可以在这个文件夹下放你随便的 `c`， `oc` 文件，舒服的使用。

umbrella.h文件  
[什么是umbrella header?](https://links.jianshu.com/go?to=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F31238761%2Fwhat-is-an-umbrella-header)

![](/images/posts/iOS/swiftmodule/swift_module_3.png)
倒入子目录.h

`umbrella + 目录`, 可以递归导出子目录下的所有`.h`

```
module OtherFile {
    header "headers.h"
    export *
    // 倒入 Subs 文件夹下所有的.h
    umbrella "Subs"
    module * { export * }
}
```

代码实例  
三个方法分别对应不同目录下的文件

```
run()
subRun()
subSubRun()

// 打印
// run
// sub run
// sub sub run
```

所以, 我们可以通过 `umbrella` 更简单的实现导出, 只需要把文件都放到子目录下, 并导出就可以了, 同时支持 `c` 和 `oc`.

### module \* { export \* } 和 export \* 的区别

如下两个 `modules` 分别用 `module * { export * }` 和 `export *` 来实现的

```
module OtherFile {
    // c file
    module CFile {
        header "file.h"
        header "filea.h"
        header "filebbb.h"
        export *
    }
    
    umbrella "Subs"
    module * { export * }
    
    // oc file
    module Test {
        requires objc
        header "Test3.h"
        header "Test2.h"
        header "Test.h"
        export *
        
        umbrella "Subs/OCSubs"
        module * { export * }
    }
}
```

上面 `OtherFile module` 编译产生:

```
import OtherFile.CFile
import OtherFile.Sub
import OtherFile.SubSubs
import OtherFile.Test
```

上面的 `module` 使用 `module * { export * }` 产生了四个子 `module`

```
module OtherFile {
    // c file
    module CFile {
        header "file.h"
        header "filea.h"
        header "filebbb.h"
        export *
    }
    
    // subs 文件夹
    umbrella "Subs"
    export * 
    
    // oc file
    module Test {
        requires objc
        header "Test3.h"
        header "Test2.h"
        header "Test.h"
        export *
        
        umbrella "Subs/OCSubs"
        module * { export * }
    }
}
```

上面 `OtherFile module` 编译产生:

```
import OtherFile.CFile
import OtherFile.Test

//
// Subsubs.h
// ModuleTest
//
// Created by Yan Hu on 2019/10/14.
// Copyright © 2019 yan. All rights reserved.
//

public func subSubRun()
//
// Sub.h
// ModuleTest
//
// Created by Yan Hu on 2019/10/14.
// Copyright © 2019 yan. All rights reserved.
//

public func subRun()
```

上面的 `module` 使用 `export *` 产生了2个子 `module` 和两个方法, 这两个方法分别属于 `Subsubs.h` 和 `Sub.h`

![](/images/posts/iOS/swiftmodule/swift_module_4.webp)
目录关系

你会发现, 使用

```
umbrella "Subs"
module * { export * }
```

进行导出, 把 subs 文件夹下所有的 `.h` 文件单独生成了一个 `subModule` (子 module)  
使用

```
umbrella "Subs"
export *
```

进行导出, 会直接把所有 `.h` 中的方法, 直接导入到当前的 `module` 中, 所以在使用的时候, 可以跟进需求来使用.

##### 参数 system 和 的介绍

```
// 参数使用
module OtherFile [system] [extern_c] {

}
```

The `system` attribute specifies that the module is a system module. When a system module is rebuilt, all of the module’s headers will be considered system headers, which suppresses warnings. This is equivalent to placing `#pragma GCC system_header` in each of the module’s headers. The form of attributes is described in the section [Attributes](https://links.jianshu.com/go?to=https%3A%2F%2Fclang.llvm.org%2Fdocs%2FModules.html%23attributes), below.

The `extern_c` attribute specifies that the module contains C code that can be used from within C++. When such a module is built for use in C++ code, all of the module’s headers will be treated as if they were contained within an implicit `extern "C"` block. An import for a module with this attribute can appear within an `extern "C"` block. No other restrictions are lifted, however: the module currently cannot be imported within an `extern "C"` block in a namespace.

### 关于 import 的使用 sub modules

以上面产生四个`sub modules` 为例, 当我在代码中直接 `import OtherFile.Test`, 按照正常逻辑是, 只导入了 `Test` 这个子模块, 所以我可以使用这个子模块的代码, 但不是这样的, 即使你只导入了这个子模块, 其他的子模块的代码依旧可以访问到, 这个可能是 `swift 5.0` 说的`Modules` 不稳定的地方?

那么怎么实现只导入部分代码来进行使用?  
可以通过 `import class OtherFile.Test.Test` 来导入 Test 这个类,  
同时这里还可以简写为 `import class OtherFile.Test`, 这样会从模块 `OtherFile` 和它的子模块中需找到 `Test` 这个类, 并且导入.  
当你使用`import class OtherFile.Test.TestSubSub` 来导入 `TestSubSub` 这个类的时候, 发现竟然依然可以导入, `TestSubSub`类明明在 `TestSubSub` 模块下, 但`OtherFile.Test.TestSubSub`依旧可以导入, 这也是 `swift 5.0` 说的`Modules` 不稳定的地方?

反正就是可以导入单个 `typealias, struct, class, enum, protocol, var, func`, 导入的方式只需要替换上面 `import class OtherFile.Test.Test` 中的 `class` 就可以了.

使用就是:  
`import struct SomeModule.WantToImportStruct`  
`import class SomeModule.WantToImportClass`  
`import enum SomeModule.WantToImportEnum`  
`...`

源码: [文中源码, 包含 c++ 使用方法](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fyansaid%2FTest%2Ftree%2Fmaster%2FModule)  
reference: [https://clang.llvm.org/docs/Modules.html#includes-as-imports](https://links.jianshu.com/go?to=https%3A%2F%2Fclang.llvm.org%2Fdocs%2FModules.html%23includes-as-imports)  
reference: [sub modules 的使用](https://links.jianshu.com/go?to=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F31625447%2Fsubmodules-in-swift)  
reference: [c++ 使用](https://www.jianshu.com/p/116c1b3f1c11)



