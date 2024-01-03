- [*虚拟环境管理*](#1)  
- [*关于 PYTHONPATH*](#2)  
- [*打包*](#3)  
- [*`if __name__ == '__main__'`*](#4)  
- [*递归与回溯*](#5)  
- [*format 函数*](#6)  
- [*np.where() 函数*](#7)  
- [*zip 函数*](#8)  
- [*绘图相关*](#9)  
- [*a.empty、a.all()、a.any()*](#10)  
- [*海象操作符*](#11)  
- [*排序，并且需要原数组的下标*](#12)  
- [*局部变量 nonlocal、全局变量 global*](#13)  
- [*URL 的参数提取问题*](#14)  
- [*swapaxes 函数*](#15)  
- [*变量的下划线*](#16)  
- [*关于 `__call__()`*](#17)  
- [*求均值、最大、最小*](#18)  
- [*input 内容的处理*](#19)  
- [*NaN 值*](#20)  
- [*subprocess*](#21)  
- [*可交互 3D 图像示例*](#22)  
- [*脚本的参数传入*](#23)  
- [*DataFrame 中 drop 的用法，删除行或者列*](#24)  
- [*生成独热编码的方式*](#25)  
- [*奇异值分解和特征值分解*](#26)  
- [*图像 color bar 设置*](#27)  
- [*文件打包下载*](#28)  
- [*mp4 转 gif*](#29)  
- [*算法题中出现的缓存*](#30)  
- [*print 的一些参数*](#31)  
- [*`zip(*nums)` 实现对矩阵的逆时针旋转*](#32)  
- [*关于 PYTHONPATH*](#33)  

<a id='1'></a>
### *虚拟环境管理*

为了避免不同项目所需要的不同版本的第三方库之间的冲突，常常需要针对性地设置不同的 Python 虚拟环境，实现项目环境隔离  
假设虚拟环境名字为：`myvirtest`  

- 方法一：venv 包  
    创建虚拟环境 `python3 -m venv myvirtest`  
    切换到目录 `myvirtest\Scripts` 下，激活虚拟环境 `activate.bat` 或者 ` Activate.ps1`  

- 方法二：virtualenv 包  
    国内 pip 镜像下载：`pip install virtualenv -i https://mirrors.aliyun.com/pypi/simple`  
    新建虚拟环境 `$ virtualenv -p python3 myvirtest`  
    进入虚拟环境 `$ source myvirtest/bin/activate`  
    若需要指定 python 版本：`$ virtualenv --python=python3.6 myvirtest`  
    
    > 注意  
    本机需要自带对应版本的 python 才可以指定虚拟环境 python 版本，例如这里本机需要有 python3.6 才行  


<a id='2'></a>
### *关于 PYTHONPATH*

设置 PYTHONPATH 环境变量的作用，https://github.com/ydf0509/pythonpathdemo  

pycharm 会自动把项目根目录加到了 PYTHONPATH  
cmd 中设置临时的环境变量：`set PYTHONPATH=项目根目录 & python run.py`  
win10/11 的 powershell：`$env:PYTHONPATH="项目根目录" & python run.py`  
linux：`export PYTHONPATH=项目根目录;python run.py`  

设置多个环境变量，linux是 : 隔开，win是 ; 隔开 `export PYTHONPATH=/codes/proj1:/codes/proj2`  

手动硬编码 sys.path 的方法（即在脚本中添加搜索路径）不可取，因为这样需要对每个脚本进行修改，费时费力  
在控制台命令行部署运行任何项目，把PYTHONPATH设置为 **项目根目录路径** 是最合适的  

运行任何python项目设置 PYTHONPATH 为当前项目根目录的 4 个好处：  
1、任意项目目录下的任意深层级文件夹下的多个脚本都可以轻松作为python运行起点  
2、不需要 `sys.path.insert`  
3、使用从项目根目录往下寻找模块，用绝对导入，写的脚本位置可以四处移动，代码非常牢固，可靠性高  
4、与 pycharm 的运行行为保持了一致  

> `sys.path` 越靠前的文件夹路径越优先被查找  


<a id='3'></a>
### *打包*

参考这里的方法四：https://blog.csdn.net/qq_37354233/article/details/123731111  
以下方法适用于 Windows 系统  
先到官网 https://www.python.org/downloads/ 找到开发所用的 Python 版本，选择下载 embeddable 那个压缩包  
之后解压到自己想要的路径下，将写好的 Python 脚本也放在同一个目录下  
将运行所需要的第三方库都复制到路径 `\python-3.9.4-embed-amd64\Lib\site-packages\` 下  
之后编写【启动.bat】文件，一般内容如下即可：  
``` bat
@echo off
setlocal enabledelayedexpansion
chcp 65001

::切换到该bat文件所在的目录下
cd %~dp0
cd 项目文件夹路径

::设置 Qt 的临时环境变量
set QT_QPA_PLATFORM_PLUGIN_PATH=..\python-3.9.4-embed-amd64\Lib\site-packages\PySide6\plugins\platforms
echo %QT_QPA_PLATFORM_PLUGIN_PATH%

..\python-3.9.4-embed-amd64\python.exe .\main.py
@pause
```
需要修改的地方就是上面第四行 python.exe 的位置和 Python 脚本 main.py 的位置  
之后双击 bat 文件，检查是否运行成功。若显示部分包缺失再手动安装  


<a id='4'></a>
### *`if __name__ == '__main__'`*

每一个模块(.py)都有 `__name__`  

- 当模块被 **直接执行** 时  
    此时 `__name__=='__main__'`  

- 而作为外部模块 **被其他模块导入** 时  
    此时 `__name__` 为 **模块文件名**，程序会执行被导入模块的 **所有代码**（所以需要将测试代码放在这个 `if __name__ == '__main__'` 的条件下）  


<a id='5'></a>
### *递归与回溯*

我们在路上走着，前面是一个多岔路口，因为我们并不知道应该走哪条路，所以我们需要尝试。尝试的过程就是一个函数。我们选择了一个方向，后来发现又有一个多岔路口，这时候又需要进行一次选择。所以我们需要在上一次尝试结果的基础上，再做一次尝试，即在函数内部再调用一次函数，这就是 **递归** 的过程。这样重复了若干次之后，发现这次选择的这条路走不通，这时候我们知道有一个路口选错了，所以通过撤销或取消之前的决策，然后进行新的选择或路径，这就是 **回溯** 的思想  

递归函数通常包括两个主要部分——基本情况（Base Case）和递归情况（Recursive Case）。基本情况是当问题被划分到最小规模时，可以直接解决的情况。递归情况是将问题分解为更小规模的子问题，并通过调用自身来解决这些子问题  

在递归过程中，每个递归调用都会在内存中形成一个称为 **调用栈** 的数据结构。调用栈存储了每个递归函数的局部变量、返回地址和其他信息。递归调用会在调用栈中形成一个栈帧，当递归结束时，栈帧会从栈顶依次弹出，从而实现逐级返回  

> 递归算法可能具有较高的时间和空间复杂度，需要考虑优化  

``` python
# 树的路径问题
class Solution:
    def binaryTreePaths(self, root):    #二叉树路径
        if not root:    #若节点为空，则返回空列表
            return []
        if not root.left and not root.right:    #若左右节点为空，则返回当前节点的值构成的列表
            return [str(root.val)]
        
        paths = []
        if root.left:
            for i in self.binaryTreePaths(root.left):    #递归左节点
                print(str(root.val), i)
                paths.append(str(root.val) + '->' + i)
        if root.right:
            for i in self.binaryTreePaths(root.right):    #递归右节点
                print(str(root.val), i)
                paths.append(str(root.val) + '->' + i)
        print(paths)
        return paths
```

``` python
# 汉诺塔问题
# 规则：每次移动柱子上的第一个盘，到另一个柱子上；大盘不能放在小盘上面
# 思路：将问题转换成子问题，要移动所有盘子到柱3上
     # 首先将柱1最底下的大盘移动到3，前提是前(N − 1)个盘子已经按顺序摆在了柱2上
     # 接下来就是一个子问题：将(N − 1)个盘从柱2移动到柱3，前提是前(N − 2)个盘子已经按顺序摆在了柱1上
     # 。。。。。。

def TowersOfHanoi(numberOfDisks, startPeg=1, endPeg=3): #共三个柱子
    """
    numberOfDisks:当前盘子的号码 总共四个盘子 号码1~4对应盘子从小到大
    startPeg:起始的柱子
    endPeg:结束的柱子
    """
    if numberOfDisks > 0:
        TowersOfHanoi(numberOfDisks-1, startPeg, 6-startPeg-endPeg) # 1+2+3=6
        print(f"Move disk {numberOfDisks} from peg {startPeg} to peg {endPeg}") #将几号盘子从几号柱子移到几号柱子
        TowersOfHanoi(numberOfDisks-1, 6-startPeg-endPeg, endPeg)


TowersOfHanoi(numberOfDisks=4) #指定4个盘子
```

``` python
# 八皇后问题：
# 规则：在8x8的棋盘上，摆上8个皇后，确保之间不会冲突（皇后的横、纵以及两个斜对角线上都不能放皇后）
# 思路：类似于暴力搜索的问题

def is_conflict(solution, newpos): #用于判断新摆放的皇后是否与之前放好的冲突
                                    # 冲突返回True
                                    # 不冲突返回False
    '''
    示例：
    solution = [(0,0), (1,2)]
    newpos = (2,3)
    '''
    for pos in solution:
        # 同行，同列，对角线都算冲突
        if pos[0] == newpos[0] or pos[1] == newpos[1] \
            or abs(pos[0] - newpos[0]) == abs(pos[1] - newpos[1]):
            return True
    return False

def play(row=0, solution=[]):
    """
    solution是一个列表，里面是皇后放置的坐标
    """
    checker = 8
    # 从第一行开始放
    if row == checker: #row等于8说明皇后摆放完毕
        yield solution #返回结果
    else:
        for i in range(checker): #否则遍历一到八列，看看能否放置皇后
            newpos = (row, i)
            if not is_conflict(solution, newpos): #如果不冲突，则继续按照这条路放置下去
                for sol in play(row+1, solution+[newpos]): #进行递归
                    # print(len(sol))
                    yield sol

n = 0
for sol in play():
    n += 1
    print(sol)

    # 可视化棋盘
    for chess in sol:
        start = chess[1] #摆放的列号
        print("🔘"*start, "🔵", "🔘"*(7-start), sep="")
    
    print('~'*30)
print(f'八皇后问题总共 {n} 种解法')
```


<a id='6'></a>
### *format 函数*

``` python
print("Batch: {:010}, Loss: {:.2f}, Accuracy: {:.2%}".format(123, 0.1234567, 0.89))
print("Batch: {:10}, Loss: {:.2f}, Accuracy: {:.2%}".format(123, 0.1234567, 0.89))
```
`:10` 表示输出的字符串长度为 10，由于值为 123，所以前面加了 7 个空格。注意若是 `:1` 或者 `:2`，小于 3 的，不影响结果  
`:.2f` 表示保留两位小数，四舍五入  
`:.2%` 将数据转换成百分比的形式，并保留两位小数  


<a id='7'></a>
### *np.where() 函数*

``` python
import numpy as np
nums = np.arange(1, 11)[::-1]
print(nums)    #nums是多维数组也是可行的
index = np.where(nums>3) #返回满足条件的下标
index[0] #返回的index是一个元组，所以这里取[0]
# 注意里面的值表示的是满足where条件的元素下标
```


<a id='8'></a>
### *zip 函数*

``` python
a = [1, 2, 3]
b = ['hello', 'world']
c = [a, b]

print('list(zip(c)):\t\t', list(zip(c)))
print('list(zip(*c)):\t\t', list(zip(*c))) #结果等价于list(zip(a, b))，zip(*)相当于把c解压，ab不再是一个整体而是一一对应
```


<a id='9'></a>
### *绘图相关*

- 不同库的多子图绘制方法  
    ``` python
    import matplotlib.pyplot as plt

    # 创建2x2的子图布局
    fig, axes = plt.subplots(2, 2)

    # 在每个子图中绘制数据
    axes[0, 0].plot(x1, y1)
    axes[0, 1].plot(x2, y2)
    axes[1, 0].plot(x3, y3)
    axes[1, 1].plot(x4, y4)

    plt.show()
    ```

    ``` python
    import seaborn as sns

    # 创建FacetGrid
    grid = sns.FacetGrid(data, col='category', row='subcategory')

    # 在每个子图中绘制数据
    grid.map(plt.plot, 'x', 'y')

    plt.show()
    ```
    
    ``` python
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go

    # 创建4个子图的图表
    fig = make_subplots(rows=2, cols=2)

    # 在每个子图中添加图形
    fig.add_trace(go.Scatter(x=x1, y=y1), row=1, col=1)
    fig.add_trace(go.Scatter(x=x2, y=y2), row=1, col=2)
    fig.add_trace(go.Scatter(x=x3, y=y3), row=2, col=1)
    fig.add_trace(go.Scatter(x=x4, y=y4), row=2, col=2)

    fig.show()
    ```

- 通过 ax 设置子图的参数  
    可以使用它来设置坐标轴、标签、标题、线条样式等  


<a id='10'></a>
### *a.empty、a.all()、a.any()*

``` python
import pandas as pd
a = pd.Series([True, False, True])

print(a.empty) #判断是否为空，是返回True，否返回False
print(a.all()) #判断是否全为True，是返回True，否返回False
print(a.any()) #判断是否存在True，是返回True，否返回False
```


<a id='11'></a>
### *海象操作符*

Walrus operator，于 Python 3.8 版本引入  
海象操作符使用符号 `:=`，允许在表达式中 **同时进行变量赋值和表达式求值**  
``` python
# 注意两边的圆括号不能少
>>> (a := 123)
123

>>> (a := [2,4,6])
[2,4,6]

>>> (a := 'hello')
'hello'

>>> (a := '  ^_^  ')
'  ^_^  '
```


<a id='12'></a>
### *排序，并且需要原数组的下标*

``` python
a = ['ab', 'abcde', 'abc', 'abcd', 'a',]
temp = sorted(enumerate(a), key=lambda x:len(x[1]), reverse=True) #根据字符串的长度降序排列，注意使用 enumerate 函数
idx = [i[0] for i in temp]    #原本字符串的位置下标
problem = [i[1] for i in temp]    #排好序后的数组 a
```

若是 numpy 数组，则可以：  
``` python
import numpy as np
a = np.array([4,2,1,100,-4])
b = a.argsort()    #直接得到各元素排好序后对应的下标
a[b]    #即排好序的数组
```


<a id='13'></a>
### *局部变量 nonlocal、全局变量 global*

详见：https://blog.csdn.net/xCyansun/article/details/79672634  

- 1、两者使用的范围不同  
    - global 关键字可以用在任何地方，包括最上层函数中和嵌套函数中，即使之前未定义该变量，global 修饰后也可以直接使用  
    - 而 nonlocal 关键字只能用于 **嵌套函数** 中，并且**要在外层函数中定义相应的局部变量**，否则会发生错误  

- 2、两者的功能不同  
    - global 关键字修饰变量后标识该变量是全局变量，对该变量进行修改就是修改全局变量  
    - 而 nonlocal 关键字修饰变量后标识该变量是上一级函数中的局部变量，如果上一级函数中不存在该局部变量，nonlocal 位置会发生错误（最上层的函数使用 nonlocal 修饰变量必定会报错）

> 注意减少 global 变量的使用，减少资源消耗  


<a id='14'></a>
### *URL 的参数提取问题*

``` python
from urllib.parse import urlparse, parse_qs

url = 'https://www.google.com/search?newwindow=1&biw=1091&bih=763'

params = parse_qs(urlparse(url).query)

print(params)
print(params['newwindow'])
print(params['biw'])
```

> 注意  
导入特定的函数会比导入整个模块更加高效  
因为导入整个模块会将整个模块的代码加载到内存中，而导入特定的函数或类 **只会加载需要的部分，可以减少内存的使用量，并减少加载时间**  
这对于大型项目或需要频繁导入的代码来说尤为重要  


<a id='15'></a>
### *swapaxes 函数*

对于 numpy 数组来说，可以快速地交换两个 axis 的位置  
``` python
import numpy as np
arr = np.arange(24).reshape((2, 3, 4)) #假设一开始的 shape 是 (2, 3, 4)

arr.swapaxes(0, 1) #交换第一个和第二个轴，变成 (3, 2, 4)

arr.swapaxes(0, 2) #交换第一个和第三个轴，变成 (4, 3, 2)

arr.swapaxes(1, 2) #交换第二个和第三个轴，变成 (2, 4, 3)
```


<a id='16'></a>
### *变量的下划线*

- 前置的单下划线：`_something`  
    约定用于 **提示** 其他程序员，此类一般 **供内部使用**  
    
    > 注意  
    通过通配符 * 导从模块中导入所有函数，Python 将不会导入前置单下划线的函数  

- 后置的单下划线：`something_`  
    防止自己定义的属性名与 Python 内置的关键字 **重名**，可以简单的加一个下划线  

- 前置的双下划线：`__something`  
    遇到这类 Python 解释器会 **重写属性名称**，避免子类中命名冲突

- 前后置的双下划线：`__something__`  
    一般不这样定义，因为双下划线常用于 `__init__`、`__call__`、`__iter__`、`__next__` 这些方法  

- 单独的下划线：`_`  
    例如 `for _ in range(n)`，充当用不到的变量  


<a id='17'></a>
### *关于 `__call__()`*

调用函数时，若需要 **额外运行某些内容**，则可以重写 `__call__()` 函数，例如  
``` python
class A:
    def __call__(self, name):
        print('我的名字是：{}'.format(name))
        res = self.forward(name) #调用下面的 forward 函数
        return res
    def forward(self, input_):
        print('forward 函数被调用了')
        print('传入参数类型是：{}'.format(type(input_)))
        return input_

>>> a = A()
>>> input_param = a('python')
我的名字是：python
forward 函数被调用了
传入参数类型是：<class 'str'>
```


<a id='18'></a>
### *求均值、最大、最小*

``` python
import numpy as np
arr = np.random.uniform(20, 40, size=(4, 5))

# 计算每行的均值，每列相加再除以列数
row_mean = arr.mean(axis=1)

# 计算每列的均值，每行相加再除以行数
col_max = arr.max(axis=0)

# 获取最小值的索引
index_min = arr.argmin()
```


<a id='19'></a>
### *input 内容的处理*

``` python
a, b, c = map(int, input().split(','))
a, b, c
```


<a id='20'></a>
### *NaN 值*

``` python
import numpy as np
print(np.NaN is np.NaN)    #True
print(np.NaN == np.NaN)    #False
```


<a id='21'></a>
### *subprocess*

``` python
# https://www.cnblogs.com/lgj8/p/12132829.html
# 用subprocess这个模块来产生子进程，并连接到子进程的标准输入/输出/错误中去，还可以得到子进程的返回值
import subprocess

# 例子
p = subprocess.Popen("df -h", shell=True, stdout=subprocess.PIPE)    #查看磁盘分区挂载情况
out = p.stdout.readlines()
for line in out:
    print(line.strip())
p.communicate()
# 使用 subprocess 模块的 Popen 调用外部程序，stdout 或 stderr 参数是 pipe
# 推荐使用 Popen.communicate()
# 因为当程序输出超过操作系统的 pipe size 时，如果使用 Popen.wait() 方式等待程序结束获取返回值，会导致死锁，程序卡在 wait() 调用上
```


<a id='22'></a>
### *可交互 3D 图像示例*

``` python
import numpy as np
import scipy.special as sc
import matplotlib.pyplot as plt
def drumhead_height(n, k, distance, angle, t):
    kth_zero = sc.jn_zeros(n, k)[-1]
    return np.cos(t) * np.cos(n*angle) * sc.jn(n, distance*kth_zero)
# 弧度
theta = np.r_[0:2*np.pi:50j]
radius = np.r_[0:1:50j]
x = np.array([r * np.cos(theta) for r in radius])
y = np.array([r * np.sin(theta) for r in radius])
z = np.array([drumhead_height(1, 1, r, theta, 0.5) for r in radius])

# 交互图像绘制
from ipywidgets import interact, fixed
# elev控制观察的角度，azim控制左右的旋转
def plot_3D(elev=20, azim=50, x=x, y=y, z=z):
    fig = plt.figure(figsize=(10, 8))
    ax = plt.subplot(projection='3d')
    ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='RdBu_r', vmin=-0.5, vmax=0.5)
    ax.view_init(elev=elev, azim=azim);
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xticks(np.arange(-1, 1.1, 0.5))
    ax.set_yticks(np.arange(-1, 1.1, 0.5))

interact(plot_3D, elev=[20, 90], azim=(-180,180),
            x=fixed(x), y=fixed(y), z=fixed(z)
);
```


<a id='23'></a>
### *脚本的参数传入*

``` python
import os
import argparse
class Parser():
    def __init__(self, description):
        self.parser = argparse.ArgumentParser(description=description)
        self.args = None
        self._parse()
    
    def _parse(self):
        """
        设置传参格式、类型、默认值、help内容
        """
        self.parser.add_argument(
            '--path', type=str, default=None,
            help='图片集合的路径')
        self.parser.add_argument(
            '--resize', type=str, default='512x512',
            help='修改图片大小为 512x512 (default: 512x12)')
        self.parser.add_argument(
            '--rename', type=str, default='no',
            help='整理修改文件名 (default: 不修改)')

        self.args = self.parser.parse_args()


description = None
print(Parser(description).args.path)
print(Parser(description).args.resize)
print(Parser(description).args.rename)
```


<a id='24'></a>
### *DataFrame 中 drop 的用法，删除行或者列*

``` python
import pandas as pd
df = {
    'DataBase':['mysql','test','test','test','test'],
    'table':['user','student','course','sc','book']
}
df = pd.DataFrame(df)

# 删除行
df.drop(index=(df.loc[df['table']=='sc'].index), inplace=False)
# 删除列
df.drop(columns=['table'])
```


<a id='25'></a>
### *生成独热编码的方式*

``` python
# 方法一
sklearn 里面的 One-HotEncoder 方法

# 方法二
pd.get_dummies()
```


<a id='26'></a>
### *奇异值分解和特征值分解*

先由一个非对称的矩阵 A 得到对称矩阵 A1 和 A2  
然后对 A1 做特征值分解得到右奇异向量和奇异值  

> 奇异值分解得到的奇异值 == 奇异矩阵特征值分解的特征值开根号  

根据公式推出左奇异向量  
最后根据 USV.T 得到原矩阵的近似矩阵  
``` python
# https://zhuanlan.zhihu.com/p/29846048
import numpy as np
A = np.array([[0, 1], [1, 1], [1, 0]])
A1 = A.T @ A    #右奇异矩阵，对称正交矩阵
A2 = A @ A.T    #左奇异矩阵
u, s, vT = np.linalg.svd(A)    #奇异值分解，适用于所有类型的矩阵，包括方阵或者非方阵。注意这里的s是一个向量，存放各个奇异值
eval1, evec1 = np.linalg.eig(A1)    #得到右奇异向量
# eval2, evec2 = np.linalg.eig(A2)    #注意不可以直接求解左奇异向量,存在正负号的问题
print(np.allclose(np.sqrt(eval1[0]), s[0]))

smat = np.zeros([u.shape[1], vT.shape[0]])    #初始化一个方阵smat，其对角线元素是s
smat[range(s.shape[0]), range(s.shape[0])] = s
print(u @ smat @ vT)

evec2 = A@evec1/np.sqrt(eval1)    #根据US=AV推出左奇异向量u
smat = np.zeros([evec2.shape[0], evec1.T.shape[0]])
smat[range(eval1.shape[0]), range(eval1.shape[0])] = np.sqrt(eval1)
# 注意若 A 不是方阵，则这样推出的左奇异向量构成的矩阵会缺少几列向量，需要补零向量
evec2 = np.append(evec2, np.zeros([evec2.shape[0], smat.shape[0]-evec2.shape[1]]), axis=1)    #右侧添零向量

print(evec2 @ smat @ evec1.T)    #重构出的近似原矩阵
```


<a id='27'></a>
### *图像 color bar 设置*

``` python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
fig, ax = plt.subplots(1,1, figsize=(10, 8))
ax = sns.heatmap(a, annot=True, annot_kws={'fontsize':20}, cbar=False)    #取消热力图自带的cbar
mycbar = ax.figure.colorbar(ax.collections[0])
mycbar.ax.tick_params(labelsize=15)

plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

plt.show()
```


<a id='28'></a>
### *文件打包下载*

``` python
!zip -q -r output.zip "\文件夹路径。。。\*"

from IPython.display import FileLink
FileLink('output.zip')
```


<a id='29'></a>
### *mp4 转 gif*

``` python
from moviepy.editor import *

clip = (VideoFileClip(r"。。。.mp4").subclip(t_start=1, t_end=2).resize(0.5))    #resize中也可以直接传入元组设置画面大小
clip.write_gif(r"。。。.gif", fps=15)
```


<a id='30'></a>
### *算法题中出现的缓存*

``` python
from functools import lru_cache
def test(a,b):
    print('开始计算a+b的值...')
    return a + b
print('1+2等于:', test(1, 2))
print('1+2等于:', test(1, 2))
# 开始计算a+b的值...
# 1+2等于: 3
# 开始计算a+b的值...
# 1+2等于: 3

print('='*10)

@lru_cache(maxsize=None) # 等价于@cache
def test(a,b):
    print('开始计算a+b的值...')
    return a + b
print('1+2等于:', test(1, 2))
print('1+2等于:', test(1, 2))    #这里会直接调用缓存中已存在的结果
# 开始计算a+b的值...
# 1+2等于: 3
# 1+2等于: 3
```


<a id='31'></a>
### *print 的一些参数*

``` python
print('hello', 'world', sep='555', flush='', end='')
```


<a id='32'></a>
### *`zip(*nums)` 实现对矩阵的逆时针旋转*

``` python
nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
print(nums)
print(list(zip(*nums)))
```


<a id='33'></a>
