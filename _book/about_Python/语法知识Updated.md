- [*常见运算符*](#1)  
- [*条件语句*](#2)  
- [*循环语句*](#3)  
- [*字符串、数字、元组、列表、字典、集合......*](#4)  
- [*函数*](#5)  
- [*类*](#6)  
- [*文件 I/O*](#7)  
- [*异常处理*](#8)  

<a id='1'></a>
### *常见运算符*

- 矩阵乘法  
    ``` python
    import numpy as np

    # 矩阵点乘，对应元素相乘
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = np.array([[1, 2, 3]])

    result = a * b
    print(result)
    ```

- 逻辑运算  
    > 若 (lens & 1) == 0，意味着 lens 的二进制表示的最低位为0，因此它对应的十进制数是偶数  
    这是一种利用位运算来判断一个数是否为偶数的常用方法  


<a id='2'></a>
### *条件语句*

- if 语句注意点  
    ``` python
    a = [1,2,3,4,5,6,7,11]
    if a.pop() < 10: #这个if条件一判断，pop就会执行
        print('hello')
    print(a) #虽然if条件不满足，没有打印出hello，但是pop()还是执行了
    ```


<a id='3'></a>
### *循环语句*


<a id='4'></a>
### *字符串、数字、元组、列表、字典、集合......*
    
- 字符串  
    ``` python
    >>> a = ['172', '168', '1', '1']; '.'.join(a)
    172.168.1.1

    >>> b = ['2022', '01', '01']; '/'.join(b)
    2022/01/01

    >>> c = 'Hello'; d = 'World'; c+d
    HelloWorld

    >>> e = [1,2,3]; f = [4,5,6]; e+f
    [1, 2, 3, 4, 5, 6]
    
    >>> e.append(f)
    [1, 2, 3, [4, 5, 6]]
    
    >>> e.extend(f)
    [1, 2, 3, 4, 5, 6]
    ```

- numpy 数组切片  
    ``` python
    import numpy as np
    a = np.arange(9).reshape(3,3)

    a1 = a[:2, 1:]

    a2 = a[2] #取出第3行

    a3 = a[2, :] #等价于a2

    a3 = a[[2], :] #等价于a2
    ```

- 字典  
    ``` python
    # 创建字典的时候不用担心括号类型
    a = [['hello', 3], ['world', 5]]
    b = [['hello', 3], ('world', 5)]
    c = (['hello', 3], ('world', 5))
    d = (('hello', 3), ('world', 5))
    print(dict(a))
    print(dict(b))
    print(dict(c))
    print(dict(d))
    ```
    
    ``` python
    import json
    # 可以理解为将字符串类型的转换成字典
    # 注意里面的键值用的是双引号
    json_data = '{"name": "Mike", "age": "30"}'
    dict_data = json.loads(json_data)

    # 将字典转换成字符串的类型
    dict_data = {"name": "Mike", "age": "30"}
    json_data = json.dumps(dict_data)
    ```

- set 集合  
    不可切片，有 pop、remove、add、update 的方法  

    > 注意：集合本身是可变对象，但是里面的元素是不可变对象  


<a id='5'></a>
### *函数*

- 内建函数  
    Python 提供了很多，比如 `print()`  

- 自定义函数  
    - 1、`def` 关键字开头
    
    - 2、传入参数和自变量放在圆括号中间
    
    - 3、函数的第一行语句可以选择存放一些函数用法说明
    
    - 4、记得 `def` 语句后面需要冒号，函数内容需要缩进
    
    - 5、`return` 表示返回一个值给调用方。`return` 后面不加东西相当于返回 `None`

- 参数
    - 位置参数：以参数名的形式出现在函数的定义中

    - 关键字参数：调用的时候通常以 `key = value` 的形式出现

    ``` python
    def test(x, y=' world', *args, **kwargs):
        #注意函数定义时候的“位置参数”必须在“关键字参数”之前
        #这里的关键字参数的默认值是world
        return x + y

    # 调用
    test('Hello')    #y作为位置参数传递，使用默认值' world'
    test('Hello', ' Mars')    #y作为位置参数传递，指定了新值' Mars'
    test('Hello', y=' Mars')    #y作为关键字参数传递，指定了新值' Mars'
    ```

    `*args` 和 `**kwargs` 被称为 **匿名参数**，其中 `*args` 是 **匿名位置参数**，`args` 类型是 **元组**，`**kwargs` 是 **匿名关键字参数**，`kwargs` 类型是 **字典**，它们经常能在源代码里面看到，是为了满足有时候 **输入的参数个数不固定** 的情况  
    我们可以发现关键字参数因为有 `key` 在，所以例如 `y=' world'` 在参数列表中的位置没有固定要求；而位置参数不同，要求摆在关键字参数前面。否则会有以下的报错信息：  
    
    > SyntaxError: non-default argument follows default argument.


- 对象
    - 可变（mutable）对象
        - list：例如 `la = [1, 2, 3, 4]` 后再赋值 `la[2] = 5`，是将 `la` 的第三个元素值更改，`la` 本身地址值没有改变
        - dict
        ......
    
    - 不可变（immutable）对象
        - strings
        - tuples
        - numbers：例如 `a=5` 后再赋值 `a=10`，这里实际是新生成一个 int 值对象 10，再让 `a` 指向它
    
    ``` python
    # 变量可以根据赋值改变类型，所以可以说是没有类型的
    >>> a = [1,2,3]
    >>> type(a)
    <class 'list'>
    
    >>> a = "Runoob"
    >>> type(a)
    <class 'str'>
    # 此处的 [1,2,3] 是 List 类型，"Runoob" 是 String 类型
    # 而变量 a 是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象
    ```

- 参数传递
    - 可变类型传参：例如 `fun(list_a)`，则是将 `list_a` 真正的传过去，修改后函数外部的 `list_a` 也会受影响
    
    - 不可变类型传参：例如 `fun(a)`，传递的只是 `a` 的值，没有影响 `a` 对象本身。比如在 `fun(a)` 内部修改 `a` 的值，只是修改另一个复制的对象，不会影响 `a` 本身

- 默认参数的值  
    应该是 **不可变的对象**，比如 None、True、False、数字或字符串。最好不要用空列表 [ ]，如需要，则先设默认值为None，之后再通过if条件语句赋以 [ ]  

    > 解释：在函数定义时，默认参数的值会保存在函数的定义中，并在每次函数调用时重用。如果使用可变对象（如列表）作为默认值，可能会导致默认值在函数调用之间意外地被修改，导致程序出错

- 匿名或内联函数  
    目标：只是想实现一些简单的函数，或者简短的计算表达式  
    lambda 表达式典型的使用场景是 **排序或数据 reduce**  
    局限：只能指定单个表达式，不能包含其他操作，例如多个语句、条件表达式、迭代以及异常处理等等  
    - 例子
        ``` python
        # 对英文名进行字典排序
        names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
        sorted(names, key=lambda name: name.split(' ')[0].lower())

        #可以指定匿名函数中变量的值
        x = 2
        b = lambda y, x=x: x + y
        ```

    - 递推表达式结合匿名函数
        ``` python
        # https://www.zhihu.com/question/56193983
        import random
        a = [[100,200], [300,600], [10,20]]
        # 方法一
        b = [lambda params=values:random.randint(*params) for values in a]

        # 方法二
        b = []
        for i in a:
            b.append( lambda x=i: random.randint(*x) )

        b[1]()
        ```

- `partial()` 方法  
    在调用函数的时候，用于给参数设置固定的值  
    ``` python
    from functools import partial

    def test(a, b, c, d):
        print(a, b, c, d)

    # 一般实例化
    s1 = test(1, 2, 3, 4)

    # 利用 partial() 固定参数
    s2 = partial(test, a=1) #此时参数 a 被固定
    s2(2, 3, 4) #只需要传入参数 b、c、d
    ```
    有时可以让原本不兼容的代码一起工作  

- 关于星号  
    如果使用在函数 **定义** 中，`*` 表示 **收集** 任意多的位置参数  
    如果使用在函数 **调用** 语法中，`*` 表示 **展开** 可迭代对象（例如列表、元组等）  

- 函数和方法的异同点  
    1、本质上一样：函数和方法都是用于完成特定功能的代码块  
    2、调用方式不同：方法是通过实例化后的对象进行调用的，因此方法属于特定的实例对象，而不同的实例对象可以调用相同的方法。而函数可以直接被调用，不需要特定的对象。  
    3、参数的不同：在方法定义时，首个参数通常命名为self，它指向调用该方法的实例对象本身。通过self参数，**方法可以访问和操作实例对象的属性和方法**。而在函数定义时，不需要指定特定的参数，可以根据需要选择是否传入参数。  


<a id='6'></a>
### *类*

- 自定义类
    - 1、类通过 `class` 关键字定义  
    - 2、类名通用习惯为首字母大写，见名知意  
    - 3、Python3 中类基本都会继承于 `object` 类，也可以不继承，两者区别不大，但后者使用 **多继承** 时可能会出现问题

- 内置的 `__init__()` 函数  
    始终在启动类时会自动调用  
    可以使用 `__init__()` 函数将值赋给对象属性  

- 类的属性  
    - 实例属性（对象属性）：不同的实例可以有不同的值  
        实例属性的修改不影响其他实例  
        属性相当于 class 中的变量，方法相当于函数，class 实例化后，可以进行调用  
        实例对象调用的本质：  
        ``` Python
        a = Student('小明', 95)
        a.get_score()
        #  |
        #  v
        # 解释器翻译结果：
        # Student.get_score(a)
        ```
    
    - 类属性：是每个实例的共有属性  
        要修改类属性，需要通过 `类名.类属性 = ...` 进行修改  

- 对象的一些操作  
    修改属性：`temp1.public='good'`  
    删除属性：`del temp1.new`  
    删除对象：`del temp1`  
    获取对象的属性、方法：`dir(obj)`  
    以字典的形式返回对象的属性：`obj.__dict__`  
    判断对象是否是某个类型：`isinstance(obj, 类型)`  

- 常用的属性
    - `__doc__`，类的说明
    
    - `__dict__`，返回对象或者类的信息
    ``` python
    Test().__doc__
    Test().__dict__
    Test().__getattribute__('public')
    ```

- self  
    在 Python 的类定义中，self 是一个特殊的参数，用于表示实例化后的对象自身  
    约定将 self 作为第一个参数传递给类方法或实例方法。虽然在Python 中，self 这个名称并不是关键字，可以选择其他名称，但是为了遵循约定和与其他 Python 开发者保持一致，一般而言习惯将该参数命名为 self  
    相当于 C++ 里面的 self 指针，Java 里面的 this 关键字。它们都指代当前对象实例本身，并使得对象能够访问自己的属性和方法  


<a id='7'></a>
### *文件 I/O*

- DataFrame 写入文件  
    ``` python
    df.to_excel('。。。.xlsx', index=False)
    df.to_csv('。。。.csv', index=False)
    ```

- 路径标准化  
    ``` python
    import os
    input_path = 'D:/jupyterproject/logo.jpg   '
    input_file = os.path.normpath(input_path.strip())
    # normpath 统一为双反斜杠类型的 \\
    ```

- 图片的读取  
    ``` python
    input_file = '???.jpg'
    from PIL import Image 
    import numpy as np

    image = Image.open(input_file) # 用PIL中的Image.open打开图像
    image = image.resize((512, 512), Image.LANCZOS)    #修改图片大小
    image = image.convert('RGB')                       #转换成RGB模式
    raw_image = np.array(image)                        #转化成numpy数组
    print(raw_image.size)

    image_PIL = Image.fromarray(
        np.uint8(raw_image).reshape((512, 512, 3)),
        mode="RGB",    #array转换成图片
    )
    ```


<a id='8'></a>
### *异常处理*

``` Python
try:
exception:
else:
finally:
```
在 try-exception 中，若没有出现问题则 exception 不会执行，那么将会执行 else 中的内容。总之 exception 和 else 二选一  
注意若 try 的异常 **没有通过 exception 指出**，系统 **还是会报错** Traceback，且终止程序。但是此时若有 finally 语句，则系统在报错之前还会执行 finally 中的内容  
一般 finally 中会时 **释放文件句柄、内存空间** 等操作  