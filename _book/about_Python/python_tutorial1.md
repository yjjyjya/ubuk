<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨参考资料</span> 
    </div> 
</div>

黑马 Python 教程：https://github.com/cess-100/python-study

---

<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨基础知识</span> 
    </div> 
</div>

### ⭕ hello world

``` python
print("hello world")
```

### ⭕ 注释

``` python
# 单行注释

'''
多行注释
第一行注释
第二行注释
第三行注释
'''
```

选中代码后，可以使用快捷键 `ctrl + /` 进行注释  

### ⭕ 数据类型

#### 🔘 常见数据类型

``` python
# int 整型
a = 1
print(type(a))


# float 浮点型
b = 1.1
print(type(b))


# bool 布尔型
c = True
print(type(c))


# str 字符串
d = '12345'
print(type(d))


# list 列表
e = [10, 20, 30]
print(type(e))


# tuple 元组
f = (10, 20, 30)
print(type(f))


# set 集合
h = {10, 20, 30}
print(type(h))


# dict 字典
j = {"name": "TOM", "age": 18}
print(type(j))
```

#### 🔘 类型转换

``` python
# 转换成浮点型
num1 = 1
str1 = '10'
print(type(float(num1)))  # float
print(float(num1))  # 1.0
print(float(str1))  # 10.0


# 转换成字符串类型
print(type(str(num1)))  # str


# 将一个序列转换成元组
list1 = [10, 20, 30]
print(tuple(list1))  # (10, 20, 30)


# 将一个序列转换成列表
t1 = (100, 200, 300)
print(list(t1))  # [100, 200, 300]


# eval() 将字符串中的数据转换成 Python 表达式原本类型
str2 = '1'
str3 = '1.1'
str4 = '(1000, 2000, 3000)'
str5 = '[1000, 2000, 3000]'
print(eval(str2))  # 1
print(eval(str3))  # 1.1
print(eval(str4))  # (1000, 2000, 3000)
print(eval(str5))  # [1000, 2000, 3000]
```

### ⭕ 格式化输出

。。。



### ⭕ 输入

`input` 会阻塞以等待用户输入，输入完成之后程序才继续向下执行  
在 Python 中，`input` 会把接收到的任意用户输入的数据都当做 **字符串** 处理  

练习示例：

``` python
password = input('请输出您的密码：')
print(f'您输入的密码是{password}')
print(type(password))    # str
```

### ⭕ 条件语句

练习示例：

``` python
import random


# 玩家出拳
player = int(input('请出拳：0-石头，1-剪刀，2-布'))
# 电脑出拳
computer = random.randint(0, 2)
print(f'电脑出{computer}')


# 判断输赢
if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print('玩家获胜')
elif player == computer:
    print('平局')
else:
    print('电脑获胜')


# 此外，条件语句还可以嵌套
```

### ⭕ 三目运算符

``` python
a = 1
b = 2
c = a if a > b else b    #如果a大于b，则将a赋值给c，否则将b赋值给c
print(c)


tmp = [66,9,31,2,3,34,13,4,78,8,55]
# 递推表达式
# result = [1 for i in tmp if i>10]
result = [1 if i>10 else 0 for i in tmp]
print(result)
# 此外还支持多重 for 循环的递推表达式
# 并且字典、集合也可以类似地这样写
```

### ⭕ while 循环

练习示例：

``` python
# 循环打印九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('%d*%d=%d' % (j, i, i * j), end='\t')
        j += 1
    print()
    i += 1


# 以及 break 和 continue 的用法
```

#### 🔘 `while ... else ...`

``` python
while 条件:
    条件成立时需要重复执行的代码
else:
    循环【正常结束】之后要执行的代码
```

> [!NOTE|style:flat]
> 注意若 `while` 中存在 `break` 或者 `return` 就不会执行 `else` 中的内容（`for ... else ...` 也是同理）  

### ⭕ 字符串

``` python
# 支持回车换行
d = """I 
am tom"""
print(type(d))
print(d)


f = 'I\'m tom'    #注意转义字符 \
print(type(f))
print(f)
```

#### 🔘 字符串切片

``` python
tmp = 'abcdefg'

print(tmp[:-2])    # 'abcde'
# print(tmp[-4:-1:-1])  # 报错
print(tmp[-1:-4:-1])    # 'gfe'
```

> [!NOTE|style:flat]
> 上述报错的代码中，下标 `-4` 到 `-1` 选取是从左到右，而步长取 `-1`，表示从右向左，所以选不出数据  
> 选取方向与步长方向不一致就选不出来  

#### 🔘 字符串的一些操作

``` python
mystr = "hello world and cess and success and Python"


# find()
print(mystr.find('and'))  # 12
print(mystr.find('and', 15, 30))  # 21
print(mystr.find('ands'))  # -1  没找到


# index()
print(mystr.index('and'))  # 12
print(mystr.index('and', 15, 30))  # 21
# print(mystr.index('ands', 15, 30)) # 报错


# count()
print(mystr.count('and'))  # 3
print(mystr.count('and', 15, 30))  # 1
print(mystr.count('ands'))  # 0
# rfind 和 rindex 同理，只是从右往左查询
# 列表也可以进行 index 和 count


new_str = mystr.replace('and', 'he', 10)    #只将前 10 个 and 替换成 he
# 字符串是不可变数据类型，所以只能重新赋值给新的变量


list2 = mystr.split('and', 2)    #只分割前 2 个 and


# capitalize() 首字母大写，其他都改小写
print(mystr.capitalize())

# title() 每个单词首字母均大写
print(mystr.title())

# lower() 全部小写
print(mystr.lower())

# upper() 全部大写
print(mystr.upper())


# lstrip() 删除左侧空白
print(mystr.lstrip())

# rstrip() 删除右侧空白
print(mystr.rstrip())

# strip() 删除两侧空白
print(mystr.strip())
```

``` python
mystr = 'hello'

# ljust() 左对齐
print(mystr.ljust(10, '*'))  # hello*****

# rjust() 右对齐
print(mystr.rjust(10, '*'))  # *****hello

# center() 居中，偶数则左侧少点
print(mystr.center(20, '*'))  # **hello***
```

``` python
# 字符串的组合
mylist = ['aa', 'bb', 'cc']
new_str = '...'.join(mylist)
```

- 常用的字符串判断  

    ``` python
    .startwith()    #以什么开头
    .endwith()    #以什么结尾
    .isalpha()    #是否全为字母
    .isdigit()    #是否全为数字
    .isalnum()    #是否字母或数字
    .isspace()    #是否全为空格
    ```

### ⭕ 列表

列表是可变类型，可以修改其内部的元素

``` python
# append 添加元素
name_list = ['tom', 'lily']
name_list.append('big')
print(name_list)


# extend 追加元素
name_list = ['tom', 'lily']
name_list.extend('big')    # 'big' 会被分成一个一个字符导入
print(name_list)
name_list = ['tom', 'lily']
name_list.extend(['big'])    # 注意传入的是列表
print(name_list)


# insert 指定下标添加
name_list = ['tom', 'lily']
name_list.insert(1, 'big')
print(name_list)
```

``` python
# 删除元素
namelist = ['tom', 'lily', 'big']
del namelist[2]
print(namelist)


namelist = ['tom', 'lily', 'big']
namelist.pop(-1)    #若不指定下标，则默认弹出最后一个元素
print(namelist)


namelist = ['tom', 'lily', 'big']
namelist.remove('big')    #删除指定元素
print(namelist)


# 清空链表
namelist = ['tom', 'lily', 'big']
namelist.clear()
print(namelist)


# 删除链表
namelist = ['tom', 'lily', 'big']
del namelist
# print(namelist)    #name 'namelist' is not defined
```

``` python
# 判断某元素是否在列表内
'hello' in ['hello', 'world', '!!!']


# 逆序列表
.reverse()


# 原地排序
.sort(key= , reverse=)
```

#### 🔘 列表的深浅拷贝

``` python
。。。。。。。。。。。。。。。。。。
```

> [!NOTE|style:flat]
> 列表的遍历优先选择 for 循环，而不是 while 循环  

``` python
# 嵌套列表
name_list = [['小明', '小红', '小绿'],
             ['Tom', 'Lily', 'Rose'],
             ['张三', '李李四', '王五']]


print(name_list[0])  # ['小明', '小红', '小绿']
print(name_list[1][1])  # Lily
```

### ⭕ 元组

元组是不可变类型

``` python
# 多个数据元组
t1 = (10, 20, 30)
print(type(t1))  # <class 'tuple'>


# 单个数据元组
t2 = (10,)
print(type(t2))  # <class 'tuple'>
# 单个数据元组不加逗号，注意类型为 int
t3 = (10)
print(type(t3))  # <class 'int'>
```

元组也有下标，也可以使用 index 和 count 方法  
不能直接对元组的元素进行修改，但是若元组中存放了列表，则可以对列表的内部元素进行修改  

### ⭕ 字典

创建字典的方法：

``` python
# 1、
{'': , '': , }
# 2、
dict(zip( , ))
```

添加和删除元素：

``` python
# 字典新增元素
dict1 = {'name': 'tom', 'age': 20, 'gender': '男'}
dict1['id'] = 110
print(dict1)

# 删除指定的键值对
del dict1['age']
print(dict1)

# 同样可以像列表一样 clear 和删除
```

获取字典元素：

``` python
# 可以直接通过中括号访问，但是若找不到 key 会报错
print(dict1.get('id', '001'))  #get方法在找不到key的时候会返回指定的默认值 
```

循环遍历字典：

``` python
for key in dict1.keys():

for value in dict1.values():

for k, v in dict1.items():
```

### ⭕ 集合

集合，没有顺序（意味着没有下标），自动去重

``` python
# 创建集合
set()

# 注意：
s = set('abcdefg')
print(s)  # {'e', 'c', 'f', 'd', 'g', 'a', 'b'}
```

添加删除元素：

``` python
s1 = {10, 20}
s1.add(100)
print(s1)


# s1.add([11,22,33])    #会报错，若需要往集合中一次性追加多个元素，请使用 update
s1.update([11,22,33,])
print(s1)


# 删除集合中的元素，即使没有对应的元素也不会报错
s1.discard(33)
```

同样可以使用 `in` 或者 `not in` 判断数据是否在集合中  
列表、元组、集合可以通过关键字相互转换 `list()` `tuple()` `set()`  

#### 🔘 enumerate 函数

``` python
list1 = ['a', 'b', 'c', 'd', 'e']
for index, value in enumerate(list1, start=1):
    print("%d, %s" % (index, value))
```

> [!NOTE|style:flat]
> 字符串、列表、元组都支持加号合并  
> 也都支持乘号翻倍  
> 字符串、列表、元组、集合、字典都支持通过 `len()` 求得长度  

### ⭕ 函数

函数是一个具有独立功能的代码块  
可以在需要的位置进行调用  
实现代码重用  

在 Python 中，函数需要先定义后使用  
return 会将结果返回给调用该函数的地方，并且使得程序退出当前函数（层），并且后面的代码都不执行  

``` python
def myfunc(a, b):
    """
    函数说明
    :param a: 参数1
    :param b: 参数2
    :return: 返回值
    """
    pass


help(myfunc)
```

函数嵌套：一个函数里面调用了另外一个函数

#### 🔘 函数的返回值类型

``` python
def return_num2():
    return 1, 2    #返回多个值时，默认元组类型，也可以是列表或者字典等等


result = return_num2()    #也可以进行解包
print(result)
```

#### 🔘 函数的参数问题

``` python
def user_info(name, age, grade=1):
    print(f'您的名字是{name}, 年龄{age}, 年级{grade}')
# 该函数有三个参数，其中 grade 带了默认值


# 调用函数
user_info('amy', 18, 2)    #全部使用【位置参数】进行调用
user_info(name='tom', age=19, grade=3)    #全部使用【关键字参数】进行调用
user_info('rola', grade=3, age=18)    #【混用】，注意位置参数需要在关键字参数前面
# user_info(name='bob', 18, grade=18)    #报错
```

因为关键字参数传入时是带有参数名的，所有前后顺序没有要求

可变参数：args、kwargs：

``` python
# 可选择传入或者不传入
def user_info(*args, **kwargs):
    print(args)    #收集所有位置参数，并作为一个元组
    print(kwargs)    #收集关键字参数，并作为一个字典
    # 都是⼀个组包的过程


user_info('TOM', 18, id='001', grade=3)
# ('TOM', 18)
# {id:'001', grade:3}
```

#### 🔘 可变与不可变类型

- 可变类型（记忆可变的即可）  
    列表
    字典
    集合

- 不可变类型  
    整型
    浮点型
    字符串
    元组

``` python
# 对于不可变类型的变量来说，变量只是指向了值所在的地址
a = 1
b = a
print(b)
print(id(a))
print(id(b))    # a 和 b 同时指向了值 1 的地址，所以 id 值相同

a = 2
print(b)  # 这里的 b 没有随 a 改变，它还是指向原来 1 的地址
print(id(a))
print(id(b))

###############################

# 对于可变类型的变量来说
aa = [10, 20]
bb = aa
print(bb)
print(id(aa))
print(id(bb))

aa.append(30)
print(bb)    #这里的 bb 会跟着 aa 改变，因为 aa 是在原地址上进行修改的
print(id(aa))
print(id(bb))
```

需要小心注意，Python 中尽量不要将 **可变类型** 的变量作为参数传入。因为它可能会因为函数的执行而改变，并且影响到后续程序

``` python
def test(a):
    print(a, id(a))

    a += a
    print(a, id(a))


c = [11, 22]
test(c)
print(c, id(c))    #这里 c 的值发生了改变
```

> [!NOTE|style:flat]
> 在 python 中，值是靠 **引用** 来传递的  

#### 🔘 函数递归

注意设置递归终止条件

``` python
# 计算 1 到 n 的数字累加和
def sum_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_numbers(n - 1)


sum = sum_numbers(10)
print(sum)
```

#### 🔘 匿名函数

``` python
fn2 = lambda: 200
print(fn2)
print(fn2())

print((lambda a, b:a + b)(1, 2))
```

#### 🔘 高阶函数

把函数作为参数传入  
高阶函数是函数式编程的体现  

``` python
def add_num(a, b, f):
    return f(a) + f(b)


# abs 是内置的求绝对值的函数
# 将其传入我们自定义的函数中来求两个数的绝对值之和
result2 = add_num(-1, 2, abs)
print(result2)
```

部分内置高阶函数：

``` python
import functools

def func1(x):
    return x ** 2


# map(func, lst)
# 将传入的函数变量 func 作用到 lst 变量的【每个元素】
# 如果要转换为列表,可以使用 list() 来转换
list1 = [1, 2, 3, 4, 5]
result = map(func1, list1)
print(result)
print(list(result))  # [1, 4, 9, 16, 25]
```

> [!NOTE|style:flat]
> Python3 的 map 返回的是迭代器，Python2 则是返回列表

``` python
# reduce(func(x,y)，lst)
# 其中 func 必须有两个参数
# 每次 func 计算的结果继续和序列的下一个元素做累计计算
def func2(a, b):
    return a + b


list2 = [1, 2, 3, 4, 5]
result = functools.reduce(func2, list2)    #计算 list2 的累加和
print(result)
```

``` python
# filter(func, lst)
# 用于过滤序列, 过滤掉不符合条件的元素, 返回⼀个 filter 对象
def func3(x):
    return x % 2 == 0    #返回布尔值，为 True 即满足条件的


list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(func3, list3)
print(result)
print(list(result))
```

函数名是一个特殊的变量，保存了函数的地址

``` python
def test():
    print("哈哈，我是一个寂寞的test！")


test()
ret = test    #定义变量 ret 获取函数 test 的地址
print(ret)

# 可以通过 ret 调用函数
ret()
```

### ⭕ 文件操作

文件的访问模式：

||||||
| --- | --- | --- | --- | --- |
| 只读 r | rb | r+ | rb+ | 不会新建文件，没有对应文件就报错 |
| 写入 w | wb | w+ | wb+ | 会自动新建文件，但是会先清空再写入 |
| 追加 a | ab | a+ | ab+ | 会自动新建文件，末尾追加写入 |

凡是有 `b` 就是 **二进制格式打开**  
凡是有 `+` 就变为 **可读可写**  
若不指定的话，默认为 `r`  

#### 🔘 文件读取

``` python
with open('文件名', 'r') as f:
    f.read(10)    # 10 表示读取【10 字节】的数据，若不指定，则读取全部数据
    f.readline()    # 只读取【一行】数据
    f.readlines()    # readlines 按照行的方式把整个文件中的内容进行一次性读取
                    # 并且返回的是个【列表】，其中每一行的数据为一个元素
    f.tell()    # 返回当前指针位置，还能控制指针的位置，感兴趣可以深入搜索
```

将数据写入文件：

``` python
old_file = open('文件名', 'rb')    # 二进制格式读取
new_file = open('文件名', 'wb')    # 二进制格式重头写入
while True:
    content = old_file.read(1024)    # 每次读取 1024 字节，即 1KB 的数据
    if len(content) == 0:    # 满足条件则说明读取完毕
        break
    new_file.write(content)    # 将数据写入新文件中
old_file.close()
new_file.close()
```

#### 🔘 os 常用文件（夹）操作

``` python
import os

os.rename(目标文件名, 新文件名)    # 文件重命名

os.remove(目标文件名)    # 删除文件

os.mkdir(文件夹名字)    # 创建文件夹，如果文件夹已存在，则会报错

os.rmdir(文件夹名字)    # 删除文件夹，若目录不为空，则无法删除

os.getcwd()    # 获取当前目录

os.chdir(目录)    # 切换目录

os.listdir(目录)    # 获取目录中的文件，返回文件名的列表
```

### ⭕ 面向对象

面向对象的特性

- 封装  
    将属性和方法写到类的里面  
    封装可以为属性和方法添加私有权限  

- 继承  
    子类默认继承父类的所有属性和方法  
    子类可以重写父类属性和方法  

- 多态  
    传入不同的对象，产生不同的结果  

``` python
class Washer:
    def __init__(self, width, height):
        # 添加实例属性
        self.width = width
        self.height = height

    def __str__(self):
        # 使用print输出对象，默认打印对象的内存地址
        # 如果类定义了__str__ 方法，就会打印从在这个方法中return 的数据
        return '这是海尔洗衣机的说明书'

    def __del__(self):
        print('对象已被删除')

    def wash(self):
        print('洗衣机洗衣服')

    def print_info(self):
        print('洗衣机的宽度是%d, 高度是%d' % (self.width, self.height))

# 创建Washer类对象
haier1 = Washer(10, 20)  # 不传参数会报错

# 使用对象带有的方法
haier1.wash()

# 添加属性
haier1.price = 3000
```

名字两侧带有双下划线的函数叫做魔法方法，指的是具有 **特殊功能** 的函数，例如：  
`__init__()` 在创建⼀个对象时默认被调用，不需要手动调用  
`__init__(self)` 中的 `self` 参数，python 解释器会自动把 当前的对象引用 传递过去  
删除对象时，python 解释器会默认调用 `__del__()` 方法  

- 经典类  
    没有显式地继承自任何类  
    默认继承自一个名为 object 的基类  
    方法解析顺序是按照 **深度优先搜索** 的方式进行的  
    
    ``` python
    class 类名:
        pass
    ```
    
- 新式类  
    显式地继承自 object 的类  
    方法解析顺序是按照 **广度优先搜索** 的方式进行的  
    
    ``` python
    class 类名(object):    
        pass
    ```

#### 🔘 类的继承问题

``` python
# 父类A
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)
# 子类B 继承父类A
class B(A):
    pass


result = B()
result.info_print()
# 子类默认继承父类的所有属性和方法，而所有类默认继承object类
# object类是顶级类或基类；其他子类叫做派生类
```

> [!NOTE|style:flat]
> `.__mro__` 方法用于查看继承顺序

多继承的情况（注意和 **多层继承** 进行区别）：

``` python
class c1(object):

class c2(object):

class c3(object):

class myc(c3, c2, c1):
    这里可以重新定义与父类同名的方法/属性，也叫重写方法/属性


print(myc.__mro__)
# (<class '__main__.myc'>, <class '__main__.c3'>, <class '__main__.c2'>, <class '__main__.c1'>, <class 'object'>)
# 当一个类有多个父类的时候，默认使用第一个父类的同名属性和方法
```

子类调用父类方法：

``` python
# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print('使用%s制作煎饼果子' % self.kongfu)


# 学校类
class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print('使用%s制作煎饼果子' % self.kongfu)


# 徒弟类
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子配方]'

    def make_cake(self):
        # 加初始化，是防止上次调用的init方法不是自己的，从而kongfu属性值不是自己的
        self.__init__()
        print('使用%s制作煎饼果子' % self.kongfu)

    # 子类调用父类的同名方法
    def make_master_cake(self):
        # 父类类名.函数()
        # 再次调用初始化方法的原因：这里想要调用父类的同名方法和属性，
        # 属性在init初始化位置，所以需要再次调用
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


daqiu = Prentice()
print(daqiu.kongfu)  # [独创煎饼果子配方]

daqiu.make_cake()
daqiu.make_master_cake()
daqiu.make_school_cake()
daqiu.make_cake()
```

父类的初始化：

``` python
# 方法一：代码冗余，如果父类类名变化，这里代码需要频繁修改
Master.__init__(self)
Master.make_cake(self)
School.__init__(self)
School.make_cake(self)


# 方法二：super()
# 1、super(当前类名, self).函数()
super(Prentice, self).__init__()
super(Prentice, self).make_cake()
# 2、 super().函数()
super().__init__()
super().make_cake()
```

`super()` 可以自动查找父类。调用顺序遵循 `__mro__` 类属性的顺序，比较适合 **单继承** 使用

#### 🔘 私有属性

它们除了非特殊手段，只能 **在类里面访问和修改**  
一般定义 `get_xx` 用来获取私有属性  
定义 `set_xx` 用来修改私有属性值  
``` python
class myc(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age    #私有属性
    def get_age(self):
        return self.__age    #获取私有属性
```

#### 🔘 私有方法

通过 `_类名__方法名` 访问  
注意，直接 `__方法名` 是无法访问的  
``` python
class myc(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def __cal_area(self):    #定义私有方法
        return self.length*self.width

tmp = myc(length=2, width=3)
tmp.__cal_area()    #报错，在类的内部可以通过self.__cal_area() 来调用私有方法，但是在类的外部是无法直接调用私有方法的
tmp._myc__cal_area()    #正常返回值，但是这样做，一定程度会破坏类的封装性
```

多态有点像高阶函数，类里面的函数调用不同的类，会有不同的输出  

### ⭕ 类

#### 🔘 类属性和实例属性

实例属性，要求 **每个对象** 为其 **单独** 开辟一份内存空间来记录数据  
而类属性为 **全类所共有**，仅占用一份内存，更加节省内存空间  

> [!NOTE|style:flat]
> 当记录的某项数据，且该数据始终保持一致时，则可以将其定义为类属性  
> 类属性只能通过类对象修改，不能通过实例对象修改

#### 🔘 类方法

需要用装饰器 `@classmethod` 来标识其为类方法  
对于类方法，第一个参数必须是类对象，一般以 `cls` 作为第一个参数  
当方法中 **需要使用类对象**（如访问私有类属性等）时，则考虑定义类方法

``` python
class Dog(object):
    __tooth = 10    #类属性

    @classmethod
    def get_tooth(cls):    #类方法一般和类属性配合使用
        return cls.__tooth
```

#### 🔘 静态方法

需要通过装饰器 `@staticmethod` 来进行修饰  
静态方法既不需要传递类对象也不需要传递实例对象（**不需要形参 cls/self**）  
静态方法能够通过 **类对象** 和 **实例对象** 去访问  

``` python
class Dog(object):
    @staticmethod
    def info_print():
        print('这是一个狗类，用于创建狗实例....')


wangcai = Dog()
Dog.info_print()    # 静态方法能够通过类对象访问
wangcai.info_print()    # 静态方法能够通过实例对象访问
```

### ⭕ 异常处理

``` python
异常传递
try:
    。。。
    try:
        。。。
    except:
        。。。
    finally:
        。。。
except:
    。。。
```
使用 `raise` 关键字可以显式地抛出异常，提供更多的异常信息和上下文，帮助调试和定位问题，而不使用 `raise` 则会隐式地抛出异常  

#### 🔘 自定义异常

``` python
# 通过继承 Exception 来自定义
class myError(Exception):
    def __init__(self, ):
        pass

    def __str__(self):    #抛出异常时会打印的内容
        return 。。。

try:
    。。。
    if 。。。:
        raise myError()    #抛出自定义异常，raise 异常类对象
except Exception as e:
    print(e)
else:
    。。。
```

### ⭕ 模块

模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和 Python 语句  
模块能定义函数，类和变量，模块里也能包含可执行的代码  

``` python
import math
print(math.sqrt(9))

############################

from math import sqrt
# 或者 from math import *
print(sqrt(9))
```

``` python
# 为模块定义别名
import matplotlib.pyplot as plt
# 同理，模块中的函数也可以定义别名
```

`if __name__ == '__main__':` 其中的 `__name__` 是系统变量，模块标识符  
自身模块运行时，`__name__` 为 `__main__` ，否则是 **当前模块的名字**  

当导入一个模块，Python 解析器对模块位置的搜索顺序是：  
1、当前目录  
2、如果不在当前目录，Python 则搜索在 PYTHONPATH 下的每个目录  
3、如果都找不到，Python 会察看默认路径。UNIX 下，默认路径一般为 /usr/local/lib/python/  
以上模块搜索路径都存储在 system 模块的 `sys.path` 变量中  

> [!NOTE|style:flat]
> 自定义文件名不要和已有模块名重复，否则导致模块功能无法使用

``` python
import time
print(time)  # <module 'time' (built-in)>

time = 1    #不会报错，可以直接覆盖
```

``` python
# mymodule.py

__all__ = ['testA']    #当外部利用 from mymodule import * 导入当前模块的时候，仅有 testA 方法会被导入


def testA():
    print('test-A')


def testB():
    print('test-B')
```

``` python
# 假设文件目录结构：
# - mypackage
#     - __init__.py
#     - mymodule1.py
#     - mymodule2.py


# 导入方法：
# 1、
import mypackage.mymodule1
mypackage.mymodule1.某方法()


# 2、
from mypackage import *
mymodule1.某方法()
# 此方式需要在包中的 __init__.py 文件添加 __all__ = [允许导入的模块]
```

`__dict__` 查看对象所有的属性或者方法




<style> 
    .note { 
        background-color: #f9f9f9; 
        border: 1px solid #ddd; 
        padding: 10px; 
        border-radius: 10px; 
        display: inline-block; 
        font-weight: bold;
        margin: 10px 0px;
    }
    .note:hover {
        animation: gradient-in 0.5s forwards;
    }
    .note:not(:hover) {
        animation: gradient-out 0.5s forwards;
    }
    @keyframes gradient-in {
        0% {
            background-color: #f9f9f9;
        }
        20% {
            background-color: #f5f5f5;
        }
        100% {
            background-color: #e1e1e1;
        }
    }
    @keyframes gradient-out {
        0% {
            background-color: #e1e1e1;
        }
        80% {
            background-color: #f5f5f5;
        }
        100% {
            background-color: #f9f9f9;
        }
    }
    .title1 { 
        font-size: 24px; 
        /* color: #333;  */
    } 
    .title2 { 
        font-size: 20px; 
        /* color: #555;  */
    } 
    .title3 { 
        font-size: 16px; 
        /* color: #777;  */
    } 
    /* .note:hover [class^="title"]{
        font-size: 30px;
        opacity: 0.6;
    } */
</style>