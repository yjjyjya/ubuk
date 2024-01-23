<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨参考资料</span> 
    </div> 
</div>

黑马 Python 教程：https://github.com/cess-100/python-study2

---

<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨系统监控信息</span> 
    </div> 
</div>

``` python
# 导入模块
import psutil
```

### ⭕ 关于 CPU

``` python
# 核心数
psutil.cpu_count(logical=False)
# 若参数 logical=False 则只会返回物理内核


# 使用率
psutil.cpu_percent(interval=0.5)
# 若加上参数 percpu=True 则会返回一个列表，包含各个核心的使用率
```

### ⭕ 关于内存

``` python
# 内存信息，包括：总容量、可用空间及占比等
psutil.virtual_memory()
# 可以通过点号访问具体的属性，例如 psutil.virtual_memory().total
```

### ⭕ 关于磁盘

``` python
# 磁盘分区信息，包括：总容量、可用空间及占比等
psutil.disk_partitions()


# 指定目录的磁盘信息
psuntil.disk_usage('/')
```

### ⭕ 关于网络

``` python
# 可以获取到收、发数据包的数量
。。。。。。
```

### ⭕ 关于用户

``` python
# 活动用户信息
psutil.users()
```

### ⭕ 保存到日志

示例：

``` python
import psutil
import datetime
import unicodedata


def align_string(text, width, alignmethod):
    """
    处理中英文混合字符串的对齐问题
    """
    text_width = sum(2 if unicodedata.east_asian_width(c) in ('F', 'W') else 1 for c in text)
    if alignmethod == 'ljust':
        tmp = text.ljust(width - text_width)
    elif alignmethod == 'rjust':
        tmp = text.rjust(width - text_width)
    elif alignmethod == 'center':
        tmp = text.center(width - text_width)
    return tmp


cpu_per = psutil.cpu_percent(interval=0.5)
memory_info = psutil.virtual_memory()
disk_info = psutil.disk_usage("/")
net_info = psutil.net_io_counters()
current_time = datetime.datetime.now().strftime("%F %T")


log_template = f"""
|{align_string('监控时间', 19, 'center')}|{align_string('CPU使用率', 19, 'center')}|{align_string('内存使用率', 19, 'center')}|{align_string('硬盘使用率', 19, 'center')}|{align_string('网络收发量', 28, 'center')}|
|{align_string('', 19, 'ljust')}|{align_string(f'(共{psutil.cpu_count(logical=False):.2f}核CPU)', 19, 'center')}|{align_string(f'(总计{memory_info.total/1024/1024/1024:.2f}G内存)', 19, 'center')}|{align_string(f'(总计{disk_info.total/1024/1024/1024:.2f}G硬盘)', 19, 'center')}|{align_string('', 28, 'ljust')}|
|{'-' * 19}|{'-' * 19}|{'-' * 19}|{'-' * 19}|{'-' * 28}|
|{align_string(current_time, 19, 'ljust')}|{align_string(f'{cpu_per}%', 19, 'ljust')}|{align_string(f'{memory_info.percent}%', 19, 'ljust')}|{align_string(f'{disk_info.percent}%', 19, 'ljust')}|{align_string(f'收:{net_info.bytes_recv}/发:{net_info.bytes_sent}', 28, 'ljust')}|
|{'-' * 19}|{'-' * 19}|{'-' * 19}|{'-' * 19}|{'-' * 28}|
"""
print(log_template)

with open('log.txt', 'a') as f:
    f.write(log_template + '\n\n')
```

若需要持续写入日志文件，可以利用 `while` 循环  
每隔一段时间去重新计算需要的指标即可  

---

<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨发送邮件</span> 
    </div> 
</div>

``` python
# 导入模块
import yagmail
```

``` python
# 先创建对象
ya_obj = yagmail.SMTP(user="发件人邮箱", password="授权码（非密码，在邮箱设置）", host="网易邮箱服务器smtp.163.com")


# 配置邮件内容
content = '。。。'


# 发送邮件
ya_obj.send('收件人邮箱', '邮件主题', content)
```

### ⭕ 实际应用

可以结合上面的监控信息  
判断当 CPU 使用率超过 80%，内存使用率超过 90% 的时候，发送邮件给指定收件人  

``` python
if cpu_per>80 or memory_info.percent>90:
    # 发送邮件。。。
```

---

<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨套接字编程</span> 
    </div> 
</div>

``` python
# 导入模块
import socket
```

### ⭕ 创建套接字

``` python
socket.socket(参数一:协议类型, 参数二:传输方式)


# IPv4 UDP 的方式
mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM(UDP))


# IPv6 TCP 的方式
mysocket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM(TCP))


# 关闭套接字
mysocket.close()
```

### ⭕ UDP 连接收、发数据

``` python
# 发送数据
.sendto(参数一:待发送数据的二进制格式, 参数二:发送方的IP和端口号)
# 示例
mysocket.sendto('hello!'.encode(), ('192.168.166.166', 8080))


# 接收数据
# recvfrom 方法会造成程序的阻塞，一直等待直到收到数据
.recvfrom(参数:数据大小，单位字节)
# 示例
mysocket.recvfrom(1024)    # 表示从套接字中接受 1024 个字节的数据
# 收到的数据为元组：(内容的二进制形式, (发送方的 IP, 发送方的端口号))
```

### ⭕ 内容解码

``` python
# 指定 UTF-8 的解码格式，且解码失败时忽略错误
recv_data = mysocket.recvfrom(1024)
recv_text = recv_data[0].decode(encoding='UTF-8', errors='ignore')
```

### ⭕ 绑定端口

收、发端的绑定方法差不多

``` python
mysocket.bind((参数一:字符串形式的IP, 参数二:整数端口号))
```

接收端的参数一 IP 为空字符串时，若计算机有多个网卡，则不同网卡的数据都能被接收  
为什么需要绑定端口号？？？  

### ⭕ 设置广播

``` python
# 默认不允许发送广播，需要开启相关权限
.setsocketopt(参数一:套接字, 参数二:广播, 参数三:广播属性布尔值)


# 示例
mysocket.setsocketopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
```

### ⭕ TCP 客户端

类似 UDP 传输  

``` python
# 创建套接字
socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
.connect(('IP地址', 端口号))

# 发送数据
.send('发送内容'.encode())

# 接收数据
.recv(1024)    #二进制形式，还需要解码
.decode()

# 关闭套接字
.close()
```

### ⭕ TCP 服务端

``` python
# 不是建立连接，而是绑定端口和 IP
.bind(('', 端口号))    # 这里的 IP 放空，便于接收数据

# 开启监听，使得套接字不能主动发送数据
.listen(128)    # 128 是允许的最大连接数

# 等待客户端连接
.accept()    # 在连接之前，程序都处于阻塞状态
            # 客户端连接后，返回新的套接字对象和一个包含IP和端口号的元组

# 使用新的套接字进行收、发数据
# 操作同上
```

可以将 accept 和收发数据操作置于 while 循环中，模拟多个客户端前后接入的情况  

### ⭕ 文件下载器

客户端发送文件名给服务端，服务端循环读取对应的文件内容，然后发送给客户端  
客户端再接收数据，循环写入到本地的文件中  
收到的数据不用再解码，直接 `file.write(recv_data)` 将二进制数据写入  

### ⭕ 模拟浏览器

通过套接字与目标 IP 建立 TCP 连接  
再拼接出请求协议，包括：请求行、请求头、请求空行  

``` python
request_line = 'GET / HTTP/1.1\r\n'
request_header = 'Host:www.com\r\n'
request_blank = '\r\n'
request_data = request_line + request_header + request_blank

"""
GET / HTTP/1.1

Host:www.com



"""
```

之后 send 请求协议，获取相应内容  

### ⭕ 模拟 Web 服务器

创建套接字后，设置 **地址重用**  

``` python
tcp_server_socket.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR, True
)
```

然后绑定端口，设置监听  
之后在 while 循环中，accept 客户端的连接  
根据接收到的请求协议，判断request_data是否为空  
为空则直接关闭客户端的连接  
不为空则拼接响应报文，包括：响应行、响应头、响应空行、响应主体  

``` python
response_line = 'HTTP/1.1 200 OK\r\n'
response_header = 'Server:Python20WS/2.1\r\n'
response_blank = '\r\n'
response_body = '<html><h>Hello World!</h></html>'
response_data = response_line + response_header + response_blank + response_body

"""
HTTP/1.1 200 OK

Server:Python20WS/2.1



<html><h>Hello World!</h></html>
"""
```

向客户端发送响应报文，最后关闭连接  

上述的响应主体可以根据客户端的请求协议 **从指定文件中以二进制形式读取** 后，与响应行等拼接后发送  
请求的资源在请求行中：`GET / HTTP/1.1\r\n`，这里是 `/`，则默认返回首页 `/index.html`  
只需要通过 `request_data.decode().find('\r\n')` 方法找到第一次出现 `\r\n` 的位置，然后将字符串拆分即可  

其他响应行  

``` python
"""
HTTP/1.1 404 Not Found\r\n
"""
```

若要进行面向对象封装：  
1、在 `__init__` 方法中创建套接字，设置地址重用，绑定端口号，开启被动监听  
2、定义启动服务器的函数，接受客户端连接  
3、定义接收信息的函数  

重要的是学习黑马教程是如何将上述问题解耦，以及模块调用的  

### ⭕ 使用命令行启动

``` python
import sys

# 获取命令行传递到程序的参数
params_list = sys.argv
# 可以通过 if 判断参数的格式，例如判断第二个参数是否是纯数字
# if not sys.argv[1].isdigit():
```

---

<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨线程</span> 
    </div> 
</div>

### ⭕ 创建子线程

``` python
import threading

# 创建子线程对象
thread_obj = threading.Thread(target=自定义的函数, args=(参数1, 参数2, ...))

# 启动子线程
thread_obj.start()
```

除了上述通过元组完成子线程传参，还有：  

``` python
# 字典传参
threading.Thread(target=自定义的函数, kwargs={'参数名1': 值1, '参数名2': 值2, ...})

# 混合使用
threading.Thread(target=自定义的函数, args=(参数1, 参数2, ...), kwargs={'参数名3': 值3, '参数名4': 值4, ...})
```

其他操作：

``` python
# 获取当前线程对象
threading.current_thread()

# 获取正在活跃的线程列表
threading.enumerate()
```

> [!NOTE|style:flat]
> 多个子线程之间可以通过定义全局变量来共享变量  
> 但是需要注意防止线程之间资源竞争，导致变量计算结果有误  

### ⭕ 线程守护

线程守护即 **子线程守护主线程**  

``` python
# 设置守护线程
t1_obj = threading.Thread(target=)
t1_obj.setDaemon(True)    #主线程结束后，子线程也结束
```

### ⭕ 自定义线程类

``` python
# 继承 threading.Thread 类
# 重写 run 方法
class MyThread(threading.Thread):

    def __init__(self, num):
        # 需要先调用父类的init方法
        super().__init__()
        self.num = num

    # 重写父类的run方法
    def run(self):
        。。。
    

mythread = MyThread(10)
# 子类从父类继承了 start() 方法，可以直接使用
mythread.start()
```

### ⭕ 多线程

``` python
# 创建 2 个子线程
t1 = threading.Thread(target=work1)
t2 = threading.Thread(target=work2)

# 启动线程
t1.start()
# 优先让 t1 线程优先执行，t1 执行完毕后，t2 才能执行
t1.join()
t2.start()
```

### ⭕ 锁

为了防止多线程出现资源竞争的现象，我们需要对资源进行适时的锁定  

#### 🔘 互斥锁

``` python
# 创建互斥锁
lock = threading.Lock()

# 上锁
lock.acquire()

# 解锁
lock.release()
```
有了互斥锁之后，当两个线程访问同一资源时，即使没有使用 `.join()` 等待一方结束，也不会出现资源竞争的情况  
需要小心出现死锁  

---

<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨进程</span> 
    </div> 
</div>

### ⭕ 创建子进程

``` python
import multiprocessing

def work1():
    pass

# 创建子进程对象，指定子进程名称为 p1
process_obj = multiprocessing.Process(target=work1, name='p1')

# 启动子进程
process_obj.start()

# 终止子进程
process_obj.terminate()
exit()
```

``` python
# 获取主进程的名称
multiprocessing.current_process()

# 获取进程的编号 process id（pid）
multiprocessing.current_process().pid()
# 或者通过 os 模块获取
os.getpid()
```

传参方式与 threading 类似  

### ⭕ 进程守护

``` python
# 子进程守护主进程
p1_obj = multiprocessing.Process(target=)
p1_obj.daemon = True
```

### ⭕ 队列

``` python
# 创建队列，设置长度为 5
queue = multiprocessing.Queue(5)

# 值进队列
queue.put(值可以是int、str、list、tuple、dict)

# 根据先进先出的原则，取出队列中的值
queue.get()
```

若队列已满，此时继续有值进队列，则队列会进入阻塞状态，默认会等待先取出值再放入新的值  
而使用 `.put_nowait(值)` 则会直接报错，不会阻塞  

若队列为空，此时继续进行取值，也是默认阻塞  
而使用 `.get_nowait(值)` 则会直接报错，不会阻塞  

``` python
# 判断队列是否已满
queue.full()

# 队列里面值的个数
queue.qsize()

# 判断队列是否为空
queue.empty()
```

队列判断可能有坑，具体的-->🔍

### ⭕ 进程之间的通信

思路：  
创建两个进程和一个队列  
其中一个进程向队列中 `put` 元素；另一个进程读取队列中的元素  
注意需要使用 `.join()` 使前者先执行完，之后才让后者读取数据  

### ⭕ 进程池

``` python
# 创建一个大小为 2 的进程池
mypool = multiprocessing.Pool(2)

# 异步对进程池中的内容执行某函数
pool.apply_async(某函数)

# 进程池不再接收新任务
mypool.close()

# 主进程等待进程池中的任务结束后再退出
mypool.join()
```

#### 🔘 进程池中的进程如何通信？

``` python
# 类似的，在进程池中创建队列
queue = multiprocessing.Manager().Queue(5)


result = pool.apply_async(write_queue, (queue,))
result.wait()
pool.apply_async(read_queue, (queue,))
# 其中的write_queue和read_queue是函数
# 利用进程池中的进程来执行这些函数，注意需要等待写操作的进程结束后，才进行读操作
```

#### 🔘 应用  

``` python
# 文件夹拷贝
pool = multiprocessing.Pool(3)
for filename in filelist:
    pool.apply_async(copy_work, (source_dir, dest_dir, filename))

pool.close()
pool.join()
# 上面的 copy_work 函数就是读取 source_dir 中的 filename 文件内容，然后写入到 dest_dir 文件夹中
```

---

<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨迭代器、生成器</span> 
    </div> 
</div>

### ⭕ 可迭代对象

可遍历对象即可迭代对象  
例如：列表、元组、字符串、字典  

检测一个对象是否可迭代  

``` python
from collections import Iterable

isinstance([1,2,3,4], Iterable)    #返回布尔值
```

> [!NOTE|style:flat]
> 若一个 **自定义类** 含有 `__iter__()` 方法，则它是一个可迭代对象；否则不是  
> 所以判断一个对象是否是可迭代对象，应该看其是否包含了 `__iter__()` 方法  

### ⭕ 迭代器

#### 🔘 特点  

记录遍历的位置  
提供下一个元素的值  

> [!NOTE|style:flat]
> `for` 循环的本质：  
> 先通过 `iter(要遍历对象)` 获取要遍历对象的迭代器  
> 再通过 `next(迭代器)` 获取下一元素  
> 此外 `for` 循环还自动帮我们捕获了 `StopIteration` 异常  

``` python
mylist = [1, 3, 5]

# 获取迭代器
my_iterator = iter(mylist)

# 获取下一元素
value1 = next(my_iterator)
value2 = next(my_iterator)
value3 = next(my_iterator)
value4 = next(my_iterator)    #报错 StopIteration
```

> [!NOTE|style:flat]
> 若一个 **自定义类** 不仅有 `__iter__()` 方法，还有 `__next__()` 方法，则它是一个迭代器类  

#### 🔘 应用  

自定义一个列表  
``` python
# 目标：
mylist = MyList()
for value in mylist:
    print(value)
```

思路：  
先定义 `MyList` 类。它具有 `__init__()` 方法；`__iter__()` 方法，**对外提供迭代器**；`addItem()` 方法，用来添加数据  
再定义迭代器类 `MyListIterator`，应用于上述 `MyList` 类的 `__iter__()` 方法中。它具有 `__init__()` 方法；获取下一个元素值的方法 `__next__()`  

### ⭕ 生成器

是特殊的迭代器，同样可以通过 `next(生成器)` 获取下一个值  

#### 🔘 创建方式  

- 列表推导式  
- 函数中使用了 `yield` 返回值  
    `yield` 会暂停程序，返回变量值，并且保存程序的运行状态，当执行 `next` 的时候就会继续从 `yield` 的位置向下执行  

> [!NOTE|style:flat]
> 生成器中可以使用 `return` 来结束  

### ⭕ 协程的实现

在 `while` 循环中，使用 `yield` 和 `sleep` 可以实现基本的协程  

调用 `gevent` 模块实现协程  
`gevent` 能够自动识别程序中的耗时操作，在耗时的时候自动切换到其他的任务  
``` python
from gevent import monkey
# 破解所有
monkey.patch_all()    #打补丁，让　gevent 识别 time.sleep()
# 若不打补丁，则需要使用 gevent.sleep()
import time
import gevent


# 指派任务
g1 = gevent.spawn(work1, 参数1, 参数2, ...)
g2 = gevent.spawn(work2, 参数1, 参数2, ...)

# 让主线程等待协程执行完毕再退出
g1.join()
g2.join()
# 或者
gevent.joinall([
    gevent.spawn(work1, 参数1, 参数2, ...),
    gevent.spawn(work2, 参数1, 参数2, ...)
])
```

---

<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨re 模块</span> 
    </div> 
</div>

### ⭕ match、search 方法

`re.match("正则表达式", "要验证/检测的字符串")`  
从字符串的 **开头位置** 匹配，可以用于验证输入的内容是否满足某种格式  

`re.search("正则表达式", "要搜索的字符串")`  
从需要检测的 **字符串中** 搜索满足正则的内容  

以上两个方法，如果匹配成功，返回 `match object` 对象  
如果匹配失败，返回 `None`  
可以通过 `.group()` 获取结果  

### ⭕ sub 方法

对 search 到的字符（串）进行替换  

``` python
import re

def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)


ret = re.sub(r"\d+", add, "hello python = 997")    #可以传入函数，对 search 到的内容进行更加多样化的替换修改
print(ret)
```

### ⭕ split 方法

根据正则表达式对字符串进行拆分  

``` python
result = re.split(":| ", "info:hello@163.com zhangsan lisi")    #根据冒号或者空格拆分
# 相比于 str.split() 更加灵活

print(result)
```

### ⭕ 贪婪与非贪婪

正则表达式默认为贪婪模式，满足表达式的情况下，尽可能多地获取内容  
怎么转换成非贪婪模式，在 `+*{}` 等符号的后面添加 `?` 符号即可  

``` python
result = re.match("aaa(\d+?)", "aaa123456")    #匹配到 1 就停止了
print(result.group())
```

### ⭕ 其他

字符串前 `r` 的作用  
让正则中的 `\` 不再是转义的特殊含义  

``` python
# result = re.match("<([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>.*</\\2></\\1>", "<html><h1>asdbj</h1></html>")
result = re.match(r"<([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>.*</\2></\1>", "<html><h1>asdbj</h1></html>")

print(result.group())
```

---

<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨SQL 语句</span> 
    </div> 
</div>

### ⭕ pymysql 的使用

``` python
import pymysql

# 建立连接对象
conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456')

# 创建游标对象
cur = conn.cursor()

# 使用游标对象执行 SQL 语句
sql = """
select * from students
"""
results = cur.execute(sql)
# 提交
conn.commit()
# 仅从查询的数据中取出一条数据
oneres = cur.fetchone()
# 嵌套元组，每个元组是一条数据
res = cur.fetchall()

# 关闭游标对象
cur.close()

# 关闭连接对象
conn.close()
```

### ⭕ SQL 注入

``` python
sql = f"""
select * from goods where name = {input_name} order by id desc
"""
# 当 input_name = ' or 1 or ' 时，执行
# select * from goods where name = '' or 1 or '' order by id desc
# 会导致注入问题


# 防止注入的写法
sql = """
select * from goods where name = %s order by id desc
"""
result = cur.execute(sql, [input_name, ])
```

---

<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨闭包</span> 
    </div> 
</div>

结构：  
1、存在函数的嵌套关系  
2、内存可以使用外层的变量  
3、外层返回内层的引用  

### ⭕ 简单闭包

``` python
def func_out(num1):
    print(num1)
    
    def func_inner(num2):
        print(num1)
        print(num2)
    
    return func_inner

ret = func_out(100)
# 调用里层函数
ret(200)


# 输出
# 100
# 100
# 200
```

> [!NOTE|style:flat]
> 如果在内层函数定义和外层同名的变量，编译器会优先使用内层的变量  
> 而此时若又在内层对该同名变量定义为 nonlocal，这意味着该变量使用的是外层函数的，这样会导致错误  

### ⭕ 装饰器

假设现在有一个 `login` 函数  

``` python
def login(username, uuuid):
    print(f'{username} 开始登录')
    return f'uuuid 为 {uuuid}'
```

请问如何在不修改源代码的情况下，为其增加登录前的验证功能？  
答案是使用装饰器  

``` python
def function_out(func):
    def function_in(username, uuuid='001'):
        print("------开始验证-------, username =", username)
        # 这里是验证操作...
        return func(username, uuuid)

    return function_in    #外部函数返回内部函数的函数名
```

方法一：

``` python
login2 = function_out(login)    #往外部函数中传入 login 函数
res = login2(username='iron', uuuid='023')    #相当于调用内部函数
print(res)
```

方法二：

``` python
# @function_out 装饰 login() 函数，将上述步骤简化
@function_out
def login(username, uuuid):
    print(f'{username} 开始登录')
    return f'uuuid 为 {uuuid}'


# 通过闭包调用外层函数
res = login(username='iron')
print(res)
```

若 `login` 函数需要传入位置参数和关键字参数也是同理  

那么，使用装饰器的时候如何传入参数呢？  
这次我们不直接传入，而是在 `function_out` 外层再套一个函数，使用局部变量即可  

``` python
def myverify(step):
    def function_out(func):
        def function_in(username, uuuid='001'):
            print("function_in step =", step)
            print("------开始验证-------, username =", username)
            # 这里是验证操作...
            return func(username, uuuid)
        return function_in    #外部函数返回内部函数的函数名

    # 返回装饰器的引用
    return function_out


@myverify("register 注册步骤")
def register(username, uuuid):
    print(f'{username} 开始注册')
    return f'uuuid 为 {uuuid}'

@myverify("login 登录步骤")
def login(username, uuuid):
    print(f'{username} 开始登录')
    return f'uuuid 为 {uuuid}'

print(register(username='iron'))
print(login(username='iron'))
```

`@myverify("register 注册步骤")` 分解为 2 步  
1、执行 `myverify("register 注册步骤")`，传入了参数，并且返回 `function_out` 引用，得到 `@function_out`  
2、之后就是同上，返回内部函数的引用 `function_in`  

### 多重装饰器

``` python
# 定义一个让文字加粗的装饰器
def makeBold(func):
    def function_in():
        return "<b>" + func() + "</b>"

    return function_in


# 定义一个让文字倾斜的装饰器
def makeItalic(func):
    def function_in():
        return "<i>" + func() + "</i>"

    return function_in


@makeBold
def test():
    return "hello world-1"

@makeItalic
def test2():
    return "hello world-2"

@makeItalic
@makeBold
def test3():
    return "hello world-3"


print(test())  # <b>hello world-1</b>
print(test2())  # <i>hello world-2</i>
print(test3())  # <i><b>hello world-3</b></i>
```

### 装饰器类

``` python
class Test(object):

    def __init__(self):
        print("----初始化----")

    def run(self):
        print("---正在运行---")

    def __call__(self, *args, **kwargs):
        print("---call---")


# 创建类对象
test = Test()
# 调用 run 方法
test.run()

test()
```

当使用 `对象名()` 此时会去调用类中的 `__call__()` 方法  
若没有定义 `__call__()` 方法，则会报错  

``` python
# 装饰器类
class Test(object):
    def __init__(self, func):
        self.func = func

    def _verify(self, *args, **kwargs):
        username = kwargs.get('username')
        print("------开始验证-------, username =", username)

    def __call__(self, *args, **kwargs):
        # print(args, kwargs)
        return self.func(*args, **kwargs)


@Test
def login(username, uuuid):
    print(f'{username} 开始登录')
    return f'uuuid 为 {uuuid}'

login._verify(username='iron')
res = login('iron', uuuid='023')
print(res)
```

---

<div class="container" style="text-align: center;">
    <div class="note">
        <span class="title1">✨其他</span> 
    </div> 
</div>

### ⭕ 如何实现想要的功能？思路分析

列出需要的功能  
设计框架，功能对应需要通过哪些函数实现  
各个函数实现的具体步骤  

### ⭕ 继承问题

假设类 `D` 继承了类 `B` 和类 `C`，而类 `B` 和类 `C` 都继承了类 `A`  
当创建 `D` 的实例 `d` 时，会按照方法解析顺序（Method Resolution Order，MRO）来确定调用父类的顺序  

在 Python 中，MRO 是通过 C3 线性化算法来确定的  
在这个算法中，首先会按照 **广度优先搜索** 的顺序来遍历继承关系图，然后保持子类在父类之前的顺序  

在这个例子中，MRO 的顺序是 `D -> B -> C -> A -> object`  
因此，在调用 `super().__init__()` 时，会按照这个顺序 **依次调用父类的 `__init__` 方法**  

### ⭕ @property

使得类中的方法可以作为属性调用
``` python
class Pager:
    def __init__(self, current_page):
        # 用户当前请求的页码（第一页、第二页...）
        self.current_page = current_page
        # 每页默认显示 10 条数据
        self.per_items = 10

    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items + 1
        return val

    @property
    def end(self):
        val = self.current_page * self.per_items
        return val


p = Pager(2)
print(p.start)  # 就是起始值，即：11
print(p.end)  # 就是结束值，即：20
```

``` python
class Goods:
    """
    python3 中默认继承 object 类
    python3 中才有 @xxx.setter @xxx.deleter
    """

    @property
    def price(self):
        print('@property')

    @price.setter
    def price(self, value):
        print('@price.setter')
    
    @price.deleter
    def price(self):
        print('@price.deleter')


obj = Goods()
obj.price
obj.price = 123
del obj.price
```

或者

``` python
class Goods:
    def get_price(self):
        print('price of goods')

    def set_price(self, value):
        print('set')
    
    def del_price(self):
        print('delete')
    
    goods = property(get_price, set_price, del_price, 'description...')


obj = Goods()
obj.goods
obj.goods = '5元'
del obj.goods
```

### ⭕ 上下文管理器实现文件操作

`with open('') as f:` 语句就是通过定义上下文方法来实现文件的操作  
下面我们尝试实现 `MyFile()` 类  

``` python
class MyFile(object):
    def __init__(self, file_name, file_model):
        # 创建实例属性
        self.file_name = file_name
        self.file_model = file_model

    # 上文方法（打开资源）
    def __enter__(self):
        # 打开文件，返回文件资源
        self.file = open(self.file_name, self.file_model)
        return self.file
    
    # 下文方法（关闭资源）
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 关闭文件资源
        self.file.close()
    

with Myfile('???.x=txt', 'r') as f:
    data = f.read()
    print(data)
```




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