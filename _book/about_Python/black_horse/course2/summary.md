# 系统监控信息

``` python
# 导入模块
import psutil
```

## 关于 CPU

``` python
# 核心数
psutil.cpu_count(logical=False)
# 若参数 logical=False 则只会返回物理内核

# 使用率
psutil.cpu_percent(interval=0.5)
# 若加上参数 percpu=True 则会返回一个列表，包含各个核心的使用率
```

## 关于内存

``` python
# 内存信息，包括：总容量、可用空间及占比等
psutil.virtual_memory()
# 可以通过点号访问具体的属性，例如 psutil.virtual_memory().total
```

## 关于磁盘

``` python
# 磁盘分区信息，包括：总容量、可用空间及占比等
psutil.disk_partitions()

# 指定目录的磁盘信息
psuntil.disk_usage('/')
```

## 关于网络

``` python
# 可以获取到收、发数据包的数量
。。。。。。
```

## 关于用户

``` python
# 活动用户信息
psutil.users()
```

## 保存到日志

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

若需要持续写入日志文件，可以利用while循环
每隔一段时间去重新计算需要的指标即可


# 发送邮件

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

## 实际应用

可以结合上面的监控信息  
判断当 CPU 使用率超过 80%，内存使用率超过 90% 的时候，发送邮件给指定收件人  
``` python
if cpu_per>80 or memory_info.percent>90:
    # 发送邮件。。。
```


# 套接字编程

``` python
# 导入模块
import socket
```

## 创建套接字

``` python
socket.socket(参数一:协议类型, 参数二:传输方式)

# IPv4 UDP 的方式
mysocket = socket.socket(socket.AF_INET(IP4), socket.SOCK_DGRAM(UDP))

# IPv6 TCP 的方式
mysocket = socket.socket(socket.AF_INET6(IP6), socket.SOCK_STREAM(TCP))

# 关闭套接字
mysocket.close()
```

## UDP 连接收、发数据

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

## 内容解码

``` python
# 指定 UTF-8 的解码格式，且解码失败时忽略错误
recv_data = mysocket.recvfrom(1024)
recv_text = recv_data[0].decode(encoding='UTF-8', errors='ignore')
```

## 绑定端口

收、发端的绑定方法差不多
``` python
mysocket.bind((参数一:字符串形式的IP, 参数二:整数端口号))
```
接收端的参数一 IP 为空字符串时，若计算机有多个网卡，则不同网卡的数据都能被接收
为什么需要绑定端口号？？？

## 设置广播

``` python
# 默认不允许发送广播，需要开启相关权限
.setsocketopt(参数一:套接字, 参数二:广播, 参数三:广播属性布尔值)

# 示例
mysocket.setsocketopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
```


# UDP 聊天室





